from decimal import *

getcontext().prec = 2

def sequence(
        seed_bet=1.00,
        desired_profit=1.00,
        items=13,
        win_reward=0.7
):
    r, count = [seed_bet], 1
    for i in range(items - 1):
        step_bet = ( sum(r) + desired_profit ) / win_reward
        r.append(step_bet)

    return r

def currency_ify(seq):
    return [ '{0:.2f}'.format(n) for n in seq ]
