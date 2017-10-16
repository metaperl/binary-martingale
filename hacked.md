# Let's get straight to The Cryptocurrency Carnage

## .25 BTC Stolen from my 1Broker account ($1,250 USD)
![](https://monosnap.com/file/DD2jfoxplmsyeoRYVdbm7GeUscgkIt)
was sent to
1Km6Q7BuW6R42XKDJrCyTcqo2wrfh5m3hx

## 20 BCC Stolen ($1,600 USD)
https://monosnap.com/file/oTjvF7kFFFSEeNDO888BQElkQpWxLR
was sent to:
8GrJvV8pjp6CuqakoosGejHKjQERdGg55D

## 10,990 Pura Stolen ($5,000 USD)
https://monosnap.com/file/DKecVcLaqW1pGIaJLd4o2QfgFo3iW2
was sent to:
PVGA6ZuBM4uGyE59AY5DkMtH21M6TzL2kb

## Exodus wallet raped for 1 BTC, 187 Salt, and 45 LTC (USD 8,000)
I dont feel like recovering the Exodus Wallet to provide
screenshots or see where they were sent. I do know that this entire
slaughter began after I posted this message in a Discord channel:


## 100,000 OKCash (USD 16,000)
was probably stolen


# How was I found?

So it is clear that I was hacked. I still recall logging into my
Windows VPS and seeing someone moving the mouse around and then I
began to move the mouse around as well... imagine that - almost like
walking in on a thief who has robbed your home, virtual style.

But anyway, I don't know the full details but can only guess:

I sent this message sent to a Discord channel
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
3 days ago. When the server was provided to me, it has a very
complicated one and I was prompted by Windows to change it. For fear
of being locked out by forgetting a complex password, I changed it to
something very simple:

    money1

That's right. Once someone had my IP, all they had to do was guess
"money1" as a password and they had access to $27,000 in funds. No, I
don't enjoy looking like an idiot in public, but if it will snap
someone out of the delusion that there are not thiefs on the prowl and
that you are running your own bank and need to be super-anal about
security, then it's what needs to be done.

# Reflections

## Centralized Security isnt so bad

I have all the addresses that my Bitcoin was sent to. Unfortunately,
because BTC can be sent to personal accounts, there is likely no
"authorized money transmitter" to recognize who these addresses belongs
to.

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

## ENCRYPT YOUR WALLET

If you take nothing else from this post remember to *encrypt your
wallet* ... don't be intimidated by that term. It simply means that a
password is needed before you can access funds or see the transaction
overview.

None of these wallets require a 2FA code to withdraw funds. Every
exchange has some form of secondary verification.

## Instant customer support

I am lucky that the server farm that I use has 24/7 customer
support. They were very responsive via live chat.

## Idle Timeout Screen Lock

Do you want to wake up in the morning to all your funds gone? Me
either. Having an idle screen timeout may be a pain to deal with every
day, but I can tell you: waking up to losing $27,000 is way more
painful.

## VPS Server Hardening

Again, if you are going to be your own bank, you have to think like a
bank. It always irritates me when I am trying to visit my online bank
account and they require me to enter extra forms of identification,
but now I know why they do it.

### 2-Factor Authentication is a MUST

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
wordpress site, imagine how many more bad guys must be out for blood
for money (actually currency but we dont need to get into [the
differences](https://www.youtube.com/watch?v=DyV0OfU3-FU) now).

So yes, change the username from `Administrator`.

# Conclusion

You are running your own bank. Treat it like one. Seriously. Before
you are episode 2 in Cryptocurrency Carnage.
