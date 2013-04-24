#!/usr/bin/python
from __future__ import print_function
import os
import sys
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# system
from collections import defaultdict

import datetime
from functools import wraps
import pdb
import pprint
import re
import sys
import time
import traceback

# pypi
from blargs   import Parser
from clint.textui import progress
from splinter import Browser

# local
import user


pp = pprint.PrettyPrinter(indent=4)

base_url = 'http://www.marketsworld.com'

action_path = dict(
    login = "",
    auctions = 'auctions'
)

one_minute    = 60
three_minutes = 3 * one_minute
ten_minutes   = 10 * one_minute
one_hour      = 3600

def martingale_sequence(start_at):
    l = [1,2,5,12,30,75,180,440,1066,2590,6290]

    if start_at:
        print("Original sequence = ", l)
        l = l[(start_at - 1):]
        print("Revised sequence  = ", l)

    return iter(l)

def url_for_action(action):
    return "{0}/{1}".format(base_url,action_path[action])

def loop_forever():
    while True: pass


def try_method(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        try:
            return fn(self, *args, **kwargs)
        except:
            print(traceback.format_exc())
            while True: pass

    return wrapper

# --- a "class" of maint window functions

def current_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M%p")


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

maintenance_window = dict(
    start  = datetime.datetime.today().replace(hour=14, minute=50),
    finish = datetime.datetime.today().replace(hour=17, minute=15),
)


def in_maintenance_window():
        """
Natalie: Hello, welcome to Markets World, how may I help you?

Terrence: hello...

Terrence: what time of the day do the programmers halt all trading activity?

Natalie: Our platform has binary trading available 24 hours 5 days a week whilst the world markets are open for trading. This is from Sunday 22:00 London (17:00 New York) to Friday at the same time.

Terrence: yes, but trading was halted yesterday.

Natalie: during 21:50 - 22:00 BST there is a 10 minute gap where all assets are close, this something occurs everyday due to how our platform was designed.

Terrence: what is "BST"? I'm in the New York time zone.

Natalie: BST means "British Summer Time"

nTerrence: Is that the same at GMT?

Natalie: 22:00 BST = 17:00 EST
"""

        current_time = datetime.datetime.now()


        # for k,v in maintenance_window.iteritems():
        #     print(k,v)

        # print(current_time)

        result = time_in_range(
            maintenance_window['start'],
            maintenance_window['finish'],
            current_time
        )
        return result

def my_time(dt):
    return dt.strftime('%I:%M%p')


class Entry(object):

    def __init__(self, user, browser, url, direction):
        self.user=user
        self.browser=browser
        self.url=url
        self.direction=direction

    def login(self):
        print("Logging in...")
        self.browser.visit(url_for_action('login'))
        self.browser.fill('user[email]', self.user['username'])
        self.browser.fill('user[password]', self.user['password'])
        button = self.browser.find_by_name('submit').first
        button.click()

    def select_asset(self):
        time.sleep(3)
        self.browser.find_link_by_text('+ ADD NEW ASSET').first.click()
        time.sleep(3)
        self.browser.find_link_by_text('Forex').first.click()
        time.sleep(6)
        button = self.browser.find_by_xpath('//a[@title="EURUSD"]')
        button.click()


    def choose_direction(self):
        time.sleep(6)
        lookup = '//*[@class="bet_button {0} button"]'.format(self.direction)
        button = self.browser.find_by_xpath(lookup)
        button.click()

    def input_stake(self, amount):
        print("[ {0} ] entering stake {1}: ".format(current_time(), amount), end="")
        input = self.browser.fill('amount', str(amount))

    def buy_button_value(self):
        button = self.browser.find_by_name('buy').first
        return button.value

    def wait_for_enabled_buy_button(self):
        while True:
            if self.buy_button_value() == 'BUY':
                break
            else:
                time.sleep(1)


    def buy(self):
        self.wait_for_enabled_buy_button()
        button = self.browser.find_by_name('buy').first
        #print 'Buy button', button
        button.click()

    def won(self, result):
        return "WON" in result

    def trade_result(self):
        """1 = win
        0 = tie
        -1 = lost"""
        table = self.browser.find_by_id('completed_investments')
        tbody = table.find_by_tag('tbody')
        tr = tbody.find_by_tag('tr').first
        result = tr['class']
        if "PUSH" in result:
            return 0
        elif "WON" in result:
            return 1
        elif "LOST" in result:
            return -1
        else:
            print(result, "is not recognized")
            sys.exit(1)

    def active_trades(self):
        active_investments_table = self.browser.find_by_xpath('//table[@id="active_investments"]')
        tbody = active_investments_table.find_by_tag('tbody').first
        try:
            if (tbody.find_by_tag('td').first)['class'] == 'dataTables_empty':
                return 0
            else:
                return 1
        except:
            print("\tsome error checking status of datatable. returning 0")
            return 0

    def wait_for_active_trade_to_finish(self):
        time.sleep(10)
        active_investments_table = self.browser.find_by_xpath('//table[@id="active_investments"]')
        tbody = active_investments_table.find_by_tag('tbody').first
        tds = tbody.find_by_tag('td')
        expiry_td = tds[0].value
        date_td = tds[5]
        date = date_td.value # Apr 22, 19:25:00
        dt = datetime.datetime.strptime(date, '%b %d, %H:%M:%S')
        n = datetime.datetime.now()
        dt = dt.replace(n.year)

        diff = dt - n
        wait_time = int(round(diff.total_seconds()) + 60)

        print("waiting", wait_time, "seconds")

        for i in progress.bar(range(wait_time)):
            time.sleep(1)


    def poll_for_active_trades(self):
        while True:
            if not self.active_trades():
                return
            else:
                time.sleep(10)

    def _trade(self, stake):
        self.input_stake(stake)
        self.buy()

        self.wait_for_active_trade_to_finish()

        print("\t -> ", end="")

        if self.trade_result() > 0:
            print("won. Let us take 60 seconds to rejoice!\n")
            time.sleep(one_minute)
            return 1
        elif self.trade_result() < 0:
            print("\tlost. Increasing stake")
            return -1
        else:
            print("draw. stay the same?")
            return self._trade(stake)


    @try_method
    def trade(self, seq, iterate=True):

        stake = seq.next()

        result = self._trade(stake)

        if result > 0:
            return
        elif result < 0:
            self.trade(seq)


    def check_for_maintenance_window(self, entered=False):
        if in_maintenance_window():
            notice = """

Halting trading... {0} is nearing/in maintenance window of
{1} to {2}. We dont want to get in the middle of
a trading sequence and have to stop.

            """
            print(notice.format(
                current_time(),
                my_time(maintenance_window['start']),
                my_time(maintenance_window['finish'])
                )
            )
            time.sleep(ten_minutes)
            return self.check_for_maintenance_window(True)
        else:
            return entered



def main(bid_url=None):
    args = dict()
    with Parser(args) as p:
        p.flag('live')
        p.flag('lower')
        p.int('start-at')

    while True:
        with Browser() as browser:

            _u = user.User()
            key = 'live' if args['live'] else 'demo'
            direction = 'lower' if args['lower'] else 'higher'
            print("Start at = {0}".format(args['start-at']))

            u = getattr(_u, key)
            e = Entry(u, browser, bid_url, direction)
            e.login()
            e.select_asset()
            e.choose_direction()

            while True:
                if e.check_for_maintenance_window():
                    break
                else:
                    s = martingale_sequence(args['start-at'])
                    e.trade(s)


if __name__ == '__main__':
    main(base_url)
