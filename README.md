binary-martingale
=================

This is a [Python](http://www.python.org) computer program to automatically trade [binary options](http://en.wikipedia.org/wiki/Binary_option) [martingale](http://en.wikipedia.org/wiki/Martingale_(betting_system)) style on MarketsWorld.

# Installation



## Install Anaconda Python

No support is provided for any other version of Python. Anaconda
Python runs on all platforms and has excellent package management.

Please
[download and install it](https://store.continuum.io/cshop/anaconda/).

## Unpack this binary martingale trader somewhere

You have two options to obtain this software. If you just want to run
the software, then the simplest thing is to [download a
zipfile](https://github.com/metaperl/binary-martingale/archive/master.zip)
and unzip it.

The other option is to [install git](http://git-scm.com/downloads) and
then type `git clone git@github.com:metaperl/binary-martingale.git`
... this is a better option because it will be simpler to update. But
requires you to [install git](http://git-scm.com/downloads)

## Install support software packages

#### Change to the binary martingale folder you just unzipped

    cd binary-martingale

#### Install the extra modules

    pip install -r requirements.txt

### Setup your login info

Copy `src\conf-example.py` to `src\conf.py` and edit it with your
login info. There are two entries there, one for your demo account and
one for your main account.

# Time to rock! Sample usages

NOTE: you must change to the `src` folder for this to work:

    cd binary-martingale\src

or just `cd src` if you are already in the `binary-martingale` folder.

    [~/prg/binary-martingale/src]$ ./main.py

Login to your demo account (configured in conf.py) and make 1 trade.

    [~/prg/binary-martingale/src]$ ./main.py --loginas live

Login to your live account (configured in conf.py) and make 1 trade.

    [~/prg/binary-martingale/src]$ ./main.py --help

Show the options to the program.

    [~/prg/binary-martingale/src/]$ ./main.py --lower

Issue a put trade (default is call).

    [~/prg/binary-martingale/src/]$ ./main.py --seed-bet 4

Make the initial bet 4 dollars instead of the default 1 dollar.

    [~/prg/binary-martingale/src/]$ ./main.py --step-profit 2

Aim for a profit of 2 dollars with each bet.

    [~/prg/binary-martingale/src/]$ ./main.py --step-reward .77

Assume Markets World will pay a 77% profit on a won wager.

    [~/prg/binary-martingale/src/]$ ./main.py --show-sequence

Show the martingale sequence that will be used for betting.

    [~/prg/binary-martingale/src/]$ ./main.py --round-step

Round all bets to even numbers.

    [~/prg/binary-martingale/src/]$ ./main.py --round-step --show-sequence

Show betting sequence when you round all bets to even numbers.

    [~/prg/binary-martingale/src/]$ ./main.py --max-hours 4

Engage in trading for 4 hours max (default is 5)

    [~/prg/binary-martingale/src/]$ ./main.py --sessions 3

Engage in trading until you win 3 times (default is 1)

    [~/prg/binary-martingale/src/]$ ./main.py --ignore-window

If this is false (which it is by default), then do not trade between
2pm and 6pm EST, because MarketsWorld resets their systems at 5pm EST
and this could interrupt a series of Martingale trades.

# Disclaimer

Download and usage of this program makes me completely free of any liability to the downloader and/or user.

# Good luck!

Bon voyage! Happy trading!

# Links

http://iwantyoutoprosper.com/income/transient/binary-options-transient/odyssey-into-binary-options/

# Authors

Programmer = Terrence Brannon.

## Contributors

The trending idea is due to Samkelo Ndlovu. I appreciate his testing on
Windows as well.
