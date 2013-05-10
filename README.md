binary-martingale
=================

This is a [Python](http://www.python.org) computer program to automatically trade [binary options](http://en.wikipedia.org/wiki/Binary_option) [martingale](http://en.wikipedia.org/wiki/Martingale_(betting_system)) style on MarketsWorld.

# Installation

## Install Python

You may already have Python installed or have [to download
it](http://python.org/download/).


## Install Pip

You may follow [these
instructions](http://www.pip-installer.org/en/latest/installing.html#installing-globally)
or install using [Mac Homebrew](http://mxcl.github.io/homebrew/)

### Not sure how to do this on OS X?

Then simply follow these steps:

First install
[virtualenv](http://www.virtualenv.org/en/latest/#installation) like
so:

    $ cd ~/Downloads
    $ curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz
    $ ls -larth
    $ tar xvfz virtualenv-1.9.1.tar.gz
    $ cd virtualenv-1.9.1
    $ [sudo] python setup.py install

Once virtualenv is installed create a virtual environment:

    $ virtualenv my-trader

Activate the virtual environment:

    $ source ./my-trader/bin/activate

Change into the virtual environment directory:

    $(my-trader) cd ./my-trader

Install the binary-martingale source code:

    $(my-trader) git clone  git://github.com/metaperl/binary-martingale.git

Install the additional packages:

    $(my-trader) pip install -r requirements.txt

That's it! Now just go to "Account configuration"


## Install required Python packages using pip

    pip install -r requirements.txt

# Account configuration

Create a demo account and/or live account at Markets World.

Copy `sample-user.py` to `user.py` and edit the username and password for
your live and/or demo accounts. The unix command would be:

    $ cp sample-user.py user.py

Type `python main.py` to run the martingale trader. It will only login
to a demo account by default. To trade your live account: type `python
main.py --live'`


### Suggestion

Inquire about when the next system upgrade will be. If they halt the
trading activity in the middle of your martingale sequence, that can
be painful!

For instance, here is what they say about the upgrade:

```
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
```
# Sample usages

## Default usage:

    [~/prg/binary-martingale]$ ./main.py

This will login to your demo account and make a series of martingale call trades (the default direction)

    [~/prg/binary-martingale]$ ./main.py --lower

Same thing, but will issue a series of put trades

    [~/prg/binary-martingale]$ ./main.py --seed-bet 4

Make the initial bet 4 dollars instead of the default 1 dollar

    [~/prg/binary-martingale]$ ./main.py --step-profit 2

Aim for a profit of 2 dollar with each bet

    [~/prg/binary-martingale]$ ./main.py --live

Trade on the live account instead of the demo account

# Disclaimer

Download and usage of this program makes me completely free of any liability to the downloader and/or user.

# Good luck!

Bon voyage! Happy trading!

# Links

-
  http://iwantyoutoprosper.com/income/transient/binary-options-transient/odyssey-into-binary-options/
-
