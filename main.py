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
import random
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

# https://sheet.zoho.com/public/thequietcenter/martingale
martseq = [1,2.86,6.94,16.86,40.95,99.45,241.51,586.53,1424.44,3459.35]
#martseq = martseq[0:9]
def martingale_sequence(start_at=0):

    global martseq

    if start_at:
        print("Original sequence = ", martseq)
        martseq = martseq[(start_at - 1):]
        print("Revised sequence  = ", martseq)

    return iter(martseq)

def show_seq():
    for i, e in enumerate(martseq):
        print(1+i, e)


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

def current_time_log_format():
    return "[ {0} ]".format(current_time())

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

maintenance_window = dict(
    start  = datetime.datetime.today().replace(hour=14, minute=50),
    finish = datetime.datetime.today().replace(hour=17, minute=05),
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

    def input_stake(self, stake_i, amount):
        print("{0} Stake {1} = ${2} ".format(current_time_log_format(), stake_i, amount))
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

    def show_progress_til_expiry(self, date_td):
        date_td
        date = date_td.value # Apr 22, 19:25:00
        dt = datetime.datetime.strptime(date, '%b %d, %H:%M:%S')
        n = datetime.datetime.now()
        dt = dt.replace(n.year)

        diff = dt - n
        wait_time = int(round(diff.total_seconds()) + 10)

        #print("waiting", wait_time, "seconds")

        for i in progress.bar(range(wait_time)):
            time.sleep(1)

    def wait_until_active_trade_is_completed(self, expiry_date_string):
        while True:
            time.sleep(1)
            try:
                table = self.browser.find_by_id('completed_investments')
                tbody = table.find_by_tag('tbody')
                latest_completed_trade_string = tbody.find_by_tag('td').first.value
                #print("Latest completed trade date: {0}. Expiry_date_string: {1}.", latest_completed_trade_string, expiry_date_string)
                if latest_completed_trade_string == expiry_date_string:
                    break
            except e:
                print("Error reading DOM: {1}".format(e.strerror))
                continue





    def wait_for_active_trade_to_finish(self):
        time.sleep(10)
        active_investments_table = self.browser.find_by_xpath('//table[@id="active_investments"]')
        tbody = active_investments_table.find_by_tag('tbody').first
        tds = tbody.find_by_tag('td')

        expiry_date_string = tds[0].value
        self.show_progress_til_expiry(tds[5])

        self.wait_until_active_trade_is_completed(expiry_date_string)




    def poll_for_active_trades(self):
        while True:
            if not self.active_trades():
                return
            else:
                time.sleep(10)

    def _trade(self, stake_i, stake):
        self.input_stake(stake_i, stake)
        self.buy()

        self.wait_for_active_trade_to_finish()

        #print("\t -> ", end="")

        if self.trade_result() > 0:
            rejoice = random.randint(60,90)
            print("*Win* Let us take", rejoice, "seconds to rejoice!\n")
            time.sleep(rejoice)
            return 1
        elif self.trade_result() < 0:
            print("Loss.")
            return -1
        else:
            print("Draw. Stake remains the same.")
            return self._trade(stake_i, stake)


    @try_method
    def trade(self, seq, iterate=True):

        for i, stake in enumerate(seq, start=1):
            result = self._trade(i, stake)

            if result > 0:
                break



    def check_for_maintenance_window(self, entered=False):
        if in_maintenance_window():
            notice = "{0} Halting trading: in/near maintenance window of {1} to {2}"
            print(notice.format(
                current_time_log_format(),
                my_time(maintenance_window['start']),
                my_time(maintenance_window['finish'])
                )
            )
            time.sleep(three_minutes)
            return self.check_for_maintenance_window(True)
        else:
            return entered



def main(bid_url=None):
    args = dict()
    with Parser(args) as p:
        p.flag('live')
        p.flag('lower')
        p.int('start-at')
        p.flag('show-sequence')

    if args['show-sequence']:
        show_seq()
        sys.exit(0)

    while True:
        with Browser() as browser:

            _u = user.User()
            key = 'live' if args['live'] else 'demo'
            direction = 'lower' if args['lower'] else 'higher'
            start_at = args['start-at']

            u = getattr(_u, key)
            e = Entry(u, browser, bid_url, direction)
            e.login()
            e.select_asset()
            e.choose_direction()

            while True:
                if e.check_for_maintenance_window():
                    pass
                else:
                    s = martingale_sequence(start_at)
                    e.trade(s)

                start_at = 0


if __name__ == '__main__':
    main(base_url)
