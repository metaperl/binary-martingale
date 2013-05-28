from decimal import *

getcontext().prec = 2

def sequence(
        seed_bet=1.00,
        desired_profit=1.00,
        step_reward=0.7,
        items=13
):
    #print seed_bet,  desired_profit, items,  step_reward

    r, count = [seed_bet], 1
    for i in range(items - 1):
        step_bet = ( sum(r) + desired_profit ) / step_reward
        r.append(step_bet)

    return r

def currency_ify(seq):
    return [ '{0:.2f}'.format(n) for n in seq ]
