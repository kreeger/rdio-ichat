import sys
import rdio
from datetime import datetime
from dateutil import tz
from appscript import *

# Get the consumer key from command line; if nonexistent, quit
consumer_key = sys.argv[1] if len(sys.argv) > 1 else None
if not consumer_key:
	print u'You must supply a consumer key as the 1st command line arg.'
	sys.exit()

# Get the consumer secret from command line; if nonexistent, quit
consumer_secret = sys.argv[2] if len(sys.argv) > 2 else None
if not consumer_key:
	print u'You must supply a consumer secret as the 2nd command line arg.'
	sys.exit()

# Get username from command line; if nonexistent, quit
vanity = sys.argv[3] if len(sys.argv) > 3 else None
if not vanity:
	print u'You must supply a username as the 3rd command line arg.'
	sys.exit()

# Instantiate our API manager.
m = rdio.Api(consumer_key, consumer_secret)

# Find the user supplied.
u = m.find_user(vanity_name=vanity)

# If the user exists, we need to get the full object, including the last song
# played by the user, the time it was played, and their username.
if (u): u = m.get(keys=[u.key,], extras=[
					'lastSongPlayed',
					'lastSongPlayTime',
					'username',])[0]
else:
	print u'User not found on Rdio.'
	sys.exit()

# Store a couple of local variables.
s = u.last_song_played
t = u.last_song_play_time

# Keep local time in a variable so we can use it easily.
local = tz.tzlocal()

# If the song has ended already we don't want to update. We want *current*.
if not (t.astimezone(local) + s.duration) > datetime.now(local):
	print "Song hasn't changed since last update."
	sys.exit()

# Formulate our status string.
status_new = u'Now Playing on Rdio: \u266B %s \u2014 %s' % (
	s.artist_name, s.name,)

# Use appscript to get the instance of iChat, and retrieve the current status.
status = app('iChat').status_message.get()
if not status == status_new:
	# As long as the status is different, set to our new status, and
	# write out to stdout that we did.
	app('iChat').status_message.set(status_new)
	print u'Status updated for %s - %s' % (
		s.artist_name, s.name,)