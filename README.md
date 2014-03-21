binary-martingale
=================

This is a [Python](http://www.python.org) computer program to automatically trade [binary options](http://en.wikipedia.org/wiki/Binary_option) [martingale](http://en.wikipedia.org/wiki/Martingale_(betting_system)) style on MarketsWorld.

# Installation



## Install Anaconda Python

No support is provided for any other version of Python. Anaconda
Python runs on all platforms and has excellent package management.

Please
[download and install it](https://store.continuum.io/cshop/anaconda/).

## Install PyPI requirements

After installing Anaconda Python, type:

    pip install MODULE

where `MODULE` is each of the libraries listed [here](https://github.com/metaperl/binary-martingale/blob/master/requirements.txt)

## Install the Markets World Binary Option Martingale Library

The binary options trading library is available as an Anaconda Python
Library [here](https://binstar.org/metaperl/marketsworld_martingale).
All you have to do to make it available to you is type:

    conda install -c https://conda.binstar.org/metaperl marketsworld_martingale

## That's it.

Time to rock!

# Sample usages

    [~/prg/binary-martingale]$ ./main.py --username bob --password superguy1

This will login to your demo account and make a series of martingale call trades (the default direction)

The `username` and `password` options will be omitted from the
rest of the samples. They are required in all cases except where you
simply want to display the martingale betting sequence that will be used.


    [~/prg/binary-martingale]$ ./main.py --lower

Same thing, but will issue a series of put trades

    [~/prg/binary-martingale]$ ./main.py --seed-bet 4

Make the initial bet 4 dollars instead of the default 1 dollar

    [~/prg/binary-martingale]$ ./main.py --step-profit 2

Aim for a profit of 2 dollar with each bet

    [~/prg/binary-martingale]$ ./main.py --step-reward .77

Assume Markets World will pay a 75% profit on a won wager.

    [~/prg/binary-martingale]$ ./main.py --show-sequence

Show the martingale sequence that will be used for betting.

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
