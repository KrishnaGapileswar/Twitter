import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def process(text, tokenizer = TweetTokenizer(), stopwords=[]):
	"""
	process text of a tweet
	lowercase
	toknize
	stopword removal
	digits remova

	"""

	text = text.lower()
	tokens = tokenizer.tokenize(text)
	return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

if __name__ == '__main__':
	fname = sys.argv[1]
	tweet_tokenizer = TweetTokenizer()
	punct = list(string.punctuation)
	stopword_list = stopwords.words('english') + punct + ['rt', 'via', '...']

	tf = Counter()
	with open(fname, 'r') as f:
		for line in f:
			tweet = json.loads(line)
			tokens = process(text=tweet['text'],
						tokenizer=tweet_tokenizer,
						stopwords=stopword_list)
			tf.update(tokens)

		for tag, count in tf.most_common(1000): #change as 1000 and verify
			print("{}: {}".format(tag,count))




	# y = [count for tag, count in tf.most_common(30)] #change as 1000 and verify
	# x = range(1, len(y)+1)


	# plt.bar(x,y)
	# plt.title("Term Frequencies")
	# plt.ylabel("Frequency")
	# plt.savefig('./term_distribution.png')

