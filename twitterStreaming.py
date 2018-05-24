import sys
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitterClient import get_twitter_auth


class CustomListener(StreamListener):
	"""Custom StreamListener from streaming twitter data"""

	def __init__(self,fname):
		safe_fname = format_filename(fname)
		self.outfile = "stream_%s.jsonl" % safe_fname


	def on_data(self, data):
		try:
			with open(self.outfile, 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			sys.stderr.write("Error on data: {}\n".format(e))
			time.sleep(5)
		return True

	def on_error(self, status):
		if status == 420:
			sys.stderr.write("Rate limit exceeded\n")
			return False
		else:
			sys.stderr.write("Error {}\n".format(status))
			return True


def format_filename(fname):
	"""Convert fname into a safe string for file name

	return string
	"""

	return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
	""" convert a character into _ if invalid

	return string

	"""

	valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
	if one_char in valid_chars:
		return one_char
	else:
		return '_'

if __name__ == '__main__':
	query = sys.argv[1:] #list of all CLI args
	query_fname = ' '.join(query) #string
	auth = get_twitter_auth()
	twitter_stream = Stream(auth, CustomListener(query_fname))
	twitter_stream.filter(track=query, async=True)