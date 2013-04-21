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
from splinter import Browser

# local
import user


pp = pprint.PrettyPrinter(indent=4)

base_url = 'http://www.marketsworld.com'

action_path = dict(
    login = "",
    auctions = 'auctions'
)

one_minute  = 60
ten_minutes = 10 * one_minute
one_hour    = 3600

def martingale_sequence():
    l = [1,2,5,12,30,75,180,440]
    return iter(l)

def url_for_action(action):
    return "{0}/{1}".format(base_url,action_path[action])

def loop_forever():
    while True: pass

def current_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M%p")


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


class Entry(object):

    def __init__(self, user, browser, url):
        self.user=user
        self.browser=browser
        self.url=url

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


    def click_higher(self):
        time.sleep(6)
        button = self.browser.find_by_xpath('//*[@class="bet_button higher button"]')
        button.click()

    def input_stake(self, amount):
        print("[ {0} ] entering stake {1}: ".format(current_time(), amount), end="")
        input = self.browser.fill('amount', str(amount))

    def buy_button_value(self):
        button = self.browser.find_by_name('buy').first
        return button.value

    def wait_for_enabled_buy_button(self):
        if self.buy_button_value() == 'BUY':
            return True
        else:
            time.sleep(1)
            return self.wait_for_enabled_buy_button()

    def buy(self):
        self.wait_for_enabled_buy_button()
        button = self.browser.find_by_name('buy').first
        #print 'Buy button', button
        button.click()

    def won(self, result):
        return "WON" in result

    def winning_result(self):
        table = self.browser.find_by_id('completed_investments')
        tbody = table.find_by_tag('tbody')
        tr = tbody.find_by_tag('tr').first
        #print "Checking for winning result in this html", tr.html
        return self.won(tr['class'])

    def active_trades(self):
        active_investments_table = self.browser.find_by_xpath('//table[@id="active_investments"]')
        tbody = active_investments_table.find_by_tag('tbody').first
        td = tbody.find_by_tag('td').first
        if td['class'] == 'dataTables_empty':
            return 0
        else:
            return 1

    def poll_for_active_trades(self):
        at = self.active_trades()
        #print "Active trades", at
        if self.active_trades() > 0:
            time.sleep(5)
            return self.poll_for_active_trades()
        else:
            return None

    def trade(self, seq):
        self.select_asset()
        self.click_higher()
        self.input_stake(seq.next())
        self.buy()
        time.sleep(60)
        self.poll_for_active_trades()
        if self.winning_result():
            print("won")
            return
        else:
            print("lost. increasing bet")
            self.trade(seq)

    def in_maintence_window(self):
        """
Natalie: Hello, welcome to Markets World, how may I help you?

Terrence: hello...

Terrence: what time of the day do the programmers halt all trading activity?

Natalie: Our platform has binary trading available 24 hours 5 days a week whilst the world markets are open for trading. This is from Sunday 22:00 London (17:00 New York) to Friday at the same time.

Terrence: yes, but trading was halted yesterday.

Natalie: during 21:50 - 22:00 BST there is a 10 minute gap where all assets are close, this something occurs everyday due to how our platform was designed.

Terrence: what is "BST"? I'm in the New York time zone.

Natalie: BST means "British Summer Time"

Terrence: Is that the same at GMT?

Natalie: 22:00 BST = 17:00 EST
"""

        current_time = datetime.datetime.now()

        maintenance_window = dict(
            start  = datetime.datetime.today().replace(hour=14, minute=50),
            finish = datetime.datetime.today().replace(hour=17, minute=50),
        )

        result = time_in_range(
            maintenance_window['start'],
            maintenance_window['end'],
            current_time
        )

    def check_for_maintenance_window(self):
        if self.in_maintenance_window():
            print("\tHalting trading... in maintenance window")
            time.sleep(ten_minutes)
            return self.check_for_maintenance_window()
        else:
            return None



def main(bid_url=None):
    args = dict()
    with Parser(args) as p:
        p.flag('live')

    with Browser() as browser:

        _u = user.User()
        key = 'live' if args['live'] else 'demo'
        u = getattr(_u, key)
        e = Entry(u, browser, bid_url)
        e.login()

        while True:
            s = martingale_sequence()
            e.trade(s)
            e.check_for_maintenance_window()

if __name__ == '__main__':
    main(base_url)
