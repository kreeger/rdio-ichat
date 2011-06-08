rdio-ichat.py
=============

About
-----

This is a python script that uses my
[python-rdio](http://github.com/kreeger/python-rdio) library (as well as a
couple of others) to communicate with Rdio and then send a status update to
iChat. **It requires you to have a developer account with Rdio, as well as the
OAuth consumer\_key and consumer\_secret that comes with it.**

It's not perfect, it requires iChat to be open at the time, and has some very
odd behavior if iChat isn't open (including opening it some times and signing
you out of iChat altogether some times). I've yet to nail that down.

Requirements
------------

You'll need my [python-rdio](http://pypi.python.org/pypi/python-rdio) package,
which installs a couple of packages that *it* needs. Then, you'll need
[appscript](http://appscript.sourceforge.net/). So…

     $ pip install python-rdio
     $ pip install appscript

That ought to do it. If you're not using `pip`, shame on you. If you're okay
with being shamed, you can replace it `pip install` with `easy_install`.

Usage
-----

In either case, just run the script like so.

    $ python rdio-ichat.py VANITY_NAME CONSUMER_KEY CONSUMER_SECRET

Voila! Your status *should* be changed in iChat. Enjoy.

[python-rdio]:     http://github.com/kreeger/python-rdio