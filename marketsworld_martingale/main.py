#!/usr/bin/env python


from __future__ import print_function
import os
import sys
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# system
from collections import defaultdict, Counter

import datetime
from functools import wraps
import itertools
import pdb
import pprint
import random
import re
import sys
import time
import traceback

# pypi
import argh
from clint.textui import progress
import numpy
from splinter import Browser

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

# local
import martingale
import timer


pp = pprint.PrettyPrinter(indent=4)

base_url = 'http://www.marketsworld.com'

action_path = dict(
    login = "",
    bonuses = 'bonuses'
)

one_minute    = 60
three_minutes = 3 * one_minute
ten_minutes   = 10 * one_minute
one_hour      = 3600

# https://sheet.zoho.com/public/thequietcenter/martingale

def hours_as_string(hours):
    if hours:
        return str(hours)
    else:
        return "not specified"

def session_as_string(i):
    if i < 0:
        return "No Limit"
    else:
        return str(i)

def mk_martseq(seed_bet, step_profit, step_reward, round_step):
    return martingale.currency_ify(
        martingale.sequence(seed_bet, step_profit, step_reward, round_step)
    )

def martingale_sequence(seed_bet, step_profit, step_reward, round_step):

    martseq = mk_martseq(seed_bet, step_profit, step_reward, round_step)

    return iter(martseq)

def show_seq(seed_bet, step_profit, step_reward, round_step):

    martseq = mk_martseq(seed_bet, step_profit, step_reward, round_step)

    s = 0.0
    gain_str = "{0}% gain on wager".format(step_reward * 100)
    print("Step\tWager\tCumulative\t{0}".format(gain_str))
    print("----\t-----\t----------\t-----------------")
    for i, e in enumerate(martseq):
        if i > 9:
            break
        e = float(e)
        s += float(e)
        p_gain = e + e * 0.7
        print("{0}\t{1}\t{2}\t\t{3:.2f}".format(1+i, e, s, p_gain))


def url_for_action(action):
    return "{0}/{1}".format(base_url, action_path[action])

def loop_forever():
    while True: pass

def wait_visible(driver, locator, by=By.XPATH, timeout=30):
    try:
        return ui.WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, locator)))
    except TimeoutException:
        return False


def try_method(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        try:
            return fn(self, *args, **kwargs)
        except:
            print(traceback.format_exc())
            while True:
                pass

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

# http://www.binaryoptionsdaily.com/forums/general-group2/daily-profits-losses-screenshots-forum6/469-to-482-martingale-at-markets-world-thread2438.3/#postid-29237
maintenance_window = dict(
    start=datetime.datetime.today().replace(hour=14, minute=30),
    finish=datetime.datetime.today().replace(hour=18, minute=05),
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

    def __init__(
            self, user, pass_, browser, direction, sessions, timer, trending
    ):
        self._user = user
        self._pass = pass_
        self.browser = browser
        self._initial_direction = direction
        self.direction = direction
        self.sessions = sessions
        self.timer = timer
        self._trending = trending
        self.steps = []

    def run_stats(self):
        s = """
Sess #\tSteps
------------------
"""
        print(s)
        for i, step in enumerate(self.steps, start=1):
            print("{0}\t{1}".format(i, step))

        c = Counter(self.steps)

        print("""
Total number of sessions {0}
Mininum number of steps: {1}
Maximum number of steps: {2}
Average number of steps: {3}
""".format(
    len(self.steps), min(self.steps), max(self.steps), numpy.mean(self.steps)))

        s = """Steps\t# of sessions with this step
--------------------------------------------"""
        print(s)
        for t in c.most_common():
            print("{0}\t{1}".format(*t))

    def login(self):
        print("Logging in...")
        self.browser.visit(url_for_action('login'))
        self.browser.fill('user[email]', self._user)
        self.browser.fill('user[password]', self._pass)
        button = self.browser.find_by_name('submit').first
        button.click()

    def get_balance(self):

        lookup = '//span[@class="balance"]'
        span = self.browser.find_by_xpath(lookup).first
        print ("Balance: {0}".format(span['data-balance']))

    def select_asset(self):
        time.sleep(3)
        self.browser.find_by_xpath(
            '//*[@id="content_header"]/div/div/div[2]/a').click()
        time.sleep(3)
        self.browser.find_link_by_text('Forex').first.click()
        time.sleep(6)
        button = self.browser.find_by_xpath('//a[@title="EURUSD"]')
        button.click()

    def choose_direction(self):
        #time.sleep(6)
        lookup = '//*[@class="bet_button {0} button"]'.format(self.direction)

        button = wait_visible(self.browser.driver, lookup)
        if button:
            button.click()
        else:
            raise("Cannot locate direction button to click")


        if self._trending:
            print("Trending: {0}".format(self._trending))
            print("Current direction:{0}.".format(self.direction))
            if self.direction == 'lower':
                self.direction = 'higher'
            elif self.direction == 'higher':
                self.direction = 'lower'
            print("New direction:{0}".format(self.direction))

    def input_stake(self, stake_i, amount):
        print("{0} Stake {1} = ${2} ".format(
            current_time_log_format(), stake_i, amount))
        self.browser.fill('amount', str(amount))

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
        active_investments_table = self.browser.find_by_xpath(
            '//table[@id="active_investments"]')
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
        date = date_td.value  # Apr 22, 19:25:00
        dt = datetime.datetime.strptime(date, '%b %d, %H:%M:%S')
        n = datetime.datetime.now()
        dt = dt.replace(n.year)

        diff = dt - n
        wait_time = int(round(diff.total_seconds()))

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
        self.choose_direction()
        self.input_stake(stake_i, stake)
        self.buy()

        self.wait_for_active_trade_to_finish()

        #print("\t ", end="")

        if self.trade_result() > 0:

            print("* ITM *")
            return 1
        elif self.trade_result() < 0:
            print("OTM")
            return -1
        else:
            print("Draw.")
            return self._trade(stake_i, stake)


    def intersession_break(self, i):
        rejoice = random.randint(60,90)
        notice = """
Session {0}/{1} completed. Pausing for {2} seconds.
{3}
========================================================
"""
        print(notice.format(i, session_as_string(self.sessions), rejoice, self.timer.status()))
        time.sleep(rejoice)


    @try_method
    def trade(self, seq, iterate=True):

        for i, stake in enumerate(seq, start=1):
            result = self._trade(i, stake)
            if result > 0:
                self.steps.append(i)
                break


    def tradeloop(self, session_number, s, ignore_window):

        if not ignore_window:
            self.check_for_maintenance_window()
        self.trade(s)

        self.intersession_break(session_number)

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



def main(username=None, password=None,
         seed_bet=1.00, step_profit=1.00, step_reward=0.70,
         round_step=False, show_sequence=False,
         lower=False, max_hours=5,
         sessions=1, nonstop=False, ignore_window=False,
         trending=False
     ):

    print("Seed bet = {0:.2f}. Step profit = {1:.2f}. Step Reward = {2}%".format(seed_bet, step_profit, step_reward*100, round_step))

    show_seq(seed_bet, step_profit, step_reward, round_step)
    if show_sequence:
        sys.exit(0)

    with Browser() as browser:

        browser.driver.set_window_size(1200,1100)

        if lower:
            direction = 'lower'
        else:
            direction = 'higher'

        if sessions:
            if sessions < 0:
                raise Exception("sessions must be a whole number")
            else:
                sessions = int(sessions)
        elif nonstop:
            sessions = -1

        hours = max_hours

        mytimer = timer.Timer(hours)

        print("Number of ITMs to take:", session_as_string(sessions))
        print("Number of hours to run:", hours_as_string(hours))

        e = Entry(username, password, browser, direction, sessions, mytimer,
                  trending
              )
        e.login()
        e.get_balance()
        e.select_asset()


        #pdb.set_trace()

        session_list = range(1, sessions + 1) if sessions > 0 else itertools.count(1)
        for session in session_list:
            s = martingale_sequence(
                seed_bet, step_profit, step_reward, round_step
            )

            e.tradeloop(session, s, ignore_window)
            if mytimer.time_over():
                print("Maximum execution hours reached.")
                break

            e.direction = e._initial_direction

        e.run_stats()
        e.browser.visit(url_for_action('bonuses'))
        e.get_balance()

def conda_main():
    argh.dispatch_command(main)

if __name__ == '__main__':
    argh.dispatch_command(main)
