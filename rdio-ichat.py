import sys
import rdio
from datetime import datetime
from dateutil import tz
from appscript import *

# Get the consumer key from command line; if nonexistent, quit
consumer_key = sys.argv[1] if len(sys.argv) > 1 else None
if not consumer_key:
	print u'You must supply a consumer key as the first command line argument.'
	sys.exit()

# Get the consumer secret from command line; if nonexistent, quit
consumer_secret = sys.argv[2] if len(sys.argv) > 2 else None
if not consumer_key:
	print u'You must supply a consumer secret as the second command line argument.'
	sys.exit()

# Get username from command line; if nonexistent, quit
vanity = sys.argv[3] if len(sys.argv) > 3 else None
if not vanity:
	print u'You must supply a username as the third command line argument.'
	sys.exit()

m = rdio.Api(consumer_key, consumer_secret)
u = m.find_user(vanity_name=vanity)
if (u): u = m.get(keys=[u.key,], extras=[
					'lastSongPlayed',
					'lastSongPlayTime',
					'username',])[0]
else:
	print u'User not found on Rdio.'
	sys.exit()

s = u.last_song_played
t = u.last_song_play_time

local = tz.tzlocal()
if not (t.astimezone(local) + s.duration) > datetime.now(local):
	print "Song hasn't changed since last update."
	sys.exit()

status_new = u'Now Playing on Rdio: \u266B %s \u2014 %s' % (
	s.artist_name, s.name,)
status = app('iChat').status_message.get()
if not status == status_new:
	app('iChat').status_message.set(status_new)
	print u'Status updated for %s - %s' % (
		s.artist_name, s.name,)