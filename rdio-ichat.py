import sys
import rdio
from datetime import datetime
from dateutil import tz
from appscript import *

# Get username from command line; if nonexistent, quit
USERNAME = sys.argv[1] if len(sys.argv) > 1 else None
if not USERNAME:
	print u'You must supply a username as a command line argument.'
	sys.exit()

m = rdio.Api('z4m9gvhwxzjpmqan2hb4zvfx', 't6G8HrRDGT')
u = m.find_user(vanity_name=USERNAME)
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
	print u'Set status %s' % status_new