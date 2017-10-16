# Let's get straight to The Cryptocurrency Carnage

Here is a rundown of the $30,000 that the hacker relieved me of:

## .25 BTC Stolen from my 1Broker account ($1,250 USD)
![ouch](https://monosnap.com/file/DD2jfoxplmsyeoRYVdbm7GeUscgkIt.png)
was sent to
1Km6Q7BuW6R42XKDJrCyTcqo2wrfh5m3hx

## 20 BCC Stolen ($1,600 USD)
![the agony](https://monosnap.com/file/oTjvF7kFFFSEeNDO888BQElkQpWxLR.png)
was sent to:
8GrJvV8pjp6CuqakoosGejHKjQERdGg55D

## 10,990 Pura Stolen ($5,000 USD)
![I cant take it anymore](https://monosnap.com/file/DKecVcLaqW1pGIaJLd4o2QfgFo3iW2.png)
was sent to:
PVGA6ZuBM4uGyE59AY5DkMtH21M6TzL2kb

## Exodus wallet raped for 1 BTC, 187 Salt, and 45 LTC (USD 8,000)
I am unable to get into my Windows VPS and take this screenshot. The
hacker removed RDP access for the account.

## 100,000 OKCash (USD 16,000)
was probably stolen. It's taking a while for the wallet to sync. But
he cleaned me out of every other open wallet, so why would this one be
any different.

# How was I found?

I still recall logging into my
Windows VPS and seeing someone moving the mouse around and then I
began to move the mouse around as well... imagine that - almost like
walking in on a thief who has robbed your home, virtual style.

I don't know how the hacker did his dirty deed. I can only guess.

The hack occurred a few hours after I sent this message sent to a
Discord channel
> I sent bitcoin from my Exodus wallet 2 hours ago and it still has not arrived at Bittrex. It shows as pending with 0/2 confirmations there... why is it taking so long... here is the transaction - https://blockchain.info/tx/a18f06e5f59b5b3840c208e22c5007a7ecc643ccb58ab865166498a2d8810876
(i'm trying to get into this IOP trade and good ol' bitcoin is taking it's jolly sweet time going from point A to point B)

## Monosnap?
By default, the screenshot tool [Monosnap](https://monosnap.com) lists
the title of the window. And I have taken plenty of screenshots that
advertised the IP of my Windows
VPS
[such as this one](https://monosnap.com/file/d5epIdkbvyJXjx0Sj7DnMEqX1FR0OM) and
posted them publicly.

Since this hack, I altered the default settings of Monosnap to remove
the option of showing the window title.

## Exodus? Jaxx?
In preparation for the 2 coming hard forks, I downloaded a few desktop
wallets. Exodus was kind enough to prompt me to back up my wallet. But
oddly enough, it did not prompt me to "encrypt my wallet" - which is a
fancy term for requiring a password before making any transactions.

## Random port scanning
While IP addresses are not stored in the blockchain, [there are some
ways to locate the IP that a transaction originated from](https://bitcoin.stackexchange.com/questions/193/how-do-i-see-the-ip-address-of-a-bitcoin-transaction). This,
and/or random port scanning was a definite part of the hack, because I
changed my password for my Windows VPS to something very simple about
3 days ago:

    money1

That's right. Once someone had my IP, all they had to do was guess a
username of "Administrator" and "money1" as a password and they had
access to $27,000 in funds. No, I don't enjoy looking like an idiot in
public, but if it will snap
even one person out of the delusion that there are not thiefs on the
prowl and that you are running your own bank and need to be super-anal
about security, then it's what needs to be done.

# Reflections

## Centralized security isnt so bad

I have all the addresses that my coins were sent to. But
because crypto can be sent anonymously and there is no central
authority, there is no registry connecting identities to addresses.

I guess if you want total freedom and autonomy you better be ready to
defend against those who want to misuse it.

## Back up your wallet frequently

Apparently when you restore from a wallet file, the wallet needs to
reply the blockchain from that point to present. So, presumably, the
more recent your wallet backup, the less time it takes to recover your
funds? Please correct me if I'm wrong here.

# Suggestions for Security

## Diversification

I'm a firm believer in not putting all your eggs in one basket. But I
did get caught with quite a few of my funds in one place in the
interest in having all of my desktop wallets in once place.

If I had used 4 remote servers and distributed my wallets to those 4
places, then I would be reporting a loss of just 6 or 7 grand
instead of this major setback.

## ENCRYPT YOUR WALLET

If you take nothing else from this post remember to *encrypt your
wallet* ... don't be intimidated by that term. It simply means that a
password is needed before you can access funds or see the transaction
overview.

None of these wallets require a 2FA code to withdraw funds. No bank or
ATM on this planet would allow funds to move without verifying the
identity of the mover in at least 2 ways.

Don't wait for the crypto-world to upgrade to bank-level security. Do
as much as you can TODAY!

# Harden your Windows remote server

I had all my funds on a Windows VPS (Virtual Private Server). I am
lucky that the server farm that I use has 24/7 customer support. They
were very responsive via live chat. What I am not lucky about is that
it is not easy to harden my VPS server against attack. More about that
later.

## Idle Timeout Screen Lock

Do you want to wake up in the morning to all your funds gone? Me
either. Having an idle screen timeout may be a pain to deal with every
day, but I can tell you: waking up to losing $27,000 is way more
painful.

## 2-Factor Authentication is a MUST

[2-Factor Authentication](https://www.securenvoy.com/two-factor-authentication/what-is-2fa.shtm),
2FA for short, just
means that there are additional layers of security besides just your
username and password. Notice how you have to have a debit card
**AND** your PIN before you can withdraw money from an ATM? Just
having your debit card is not enough. Unfortuntely, my windows server
did not have 2FA enabled.

Once the hacker guessed username=Administrator, password=money1, he
(or she!) was in. No need to enter a code from my cell phone,
nothing.

And that is what you need to change if you do decide to use a remote
windows server to store your funds.

While
[it does seem tortuous to setup 2-Factor Authentication on Windows](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-plan-mfa) certain
VPS providers have made it easy. For instance, you can be done with
the process
in
[a few easy steps at ServerIntellect](https://www.serverintellect.com/support/2-factor/rdp-2-factor-login/).

## Restrict IP access

If you are the only one accessing your machine, do not allow any and
all IP addresses to access your machine

## Change the administrative username

On a daily basis, [my wordpress site receives about 5-10 attempts to
break-in using the admin username](https://monosnap.com/file/iS2FujOIhOxxqlSxLL6z4nszQNGUH9).

That's right. A measly wordpress site with a bunch of meaningless
posts. So if there is that much interest in wrongdoing for a measly
wordpress site, imagine how many more bad guys must be out for my
money? Actually they are out for my currency, not my money but we dont
need to get
into [the differences](https://www.youtube.com/watch?v=DyV0OfU3-FU)
now).

So yes, change the username from `Administrator`.

# Conclusion

You are running your own bank. Treat it like one. Seriously. Before
you are episode 2 in Cryptocurrency Carnage.
