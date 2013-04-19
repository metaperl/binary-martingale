#!/usr/bin/python

# system
from collections import defaultdict
from functools import wraps
import pdb
import pprint
import re
import sys
import time
import traceback

# pypi
from splinter import Browser

# local
import user as userdata


pp = pprint.PrettyPrinter(indent=4)

base_url = 'http://www.marketsworld.com'

action_path = dict(
    login = "",
    auctions = 'auctions'
)

one_minute  = 60
ten_minutes = 10 * one_minute

def martingale_sequence():
    l = [1,2,5,12,30,75,180,440]
    return iter(l)

def url_for_action(action):
    return "{0}/{1}".format(base_url,action_path[action])

def loop_forever():
    while True: pass



class Entry(object):

    def __init__(self, user, browser, url):
        self.user=user
        self.browser=browser
        self.url=url

    def login(self):
        print "Logging in..."
        self.browser.visit(url_for_action('login'))
        self.browser.fill('user[email]', self.user['username'])
        self.browser.fill('user[password]', self.user['password'])
        button = self.browser.find_by_name('submit').first
        button.click()

    def click_higher(self):
        button = self.browser.find_by_xpath('//*[@class="bet_button higher button"]')
        button.click()

    def input_stake(self, amount):
        print "Entering stake", amount
        input = self.browser.fill('amount', str(amount))

    def buy(self):
        time.sleep(2)
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
            time.sleep(30)
            return self.poll_for_active_trades()
        else:
            return None

    def trade(self, seq):
        time.sleep(3)
        self.click_higher()
        self.input_stake(seq.next())
        self.buy()
        time.sleep(60)
        self.poll_for_active_trades()
        if self.winning_result():
            print "won"
            return
        else:
            print "lost. increasing bet"
            self.trade(seq)


def main(bid_url=None):
    with Browser() as browser:

        for user in userdata.users:
            e = Entry(user, browser, bid_url)
            e.login()

            while True:
                s = martingale_sequence()
                e.trade(s)


if __name__ == '__main__':
    main(base_url)
