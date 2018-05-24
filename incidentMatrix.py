import sys
from collections import Counter
import json


def get_hashtags(tweet):
	entities = tweet.get('entities', {})
	hashtags = entities.get('hashtags', [])
	return [tag['text'].lower() for tag in hashtags]


if __name__ == '__main__':
	fname = sys.argv[1]
	tweetnumber = 0
	with open(fname, 'r') as f:
		hashtags = Counter()
		for line in f:
			tweet = json.loads(line)
			tweetnumber+=1
			hashtags_in_tweet = get_hashtags(tweet)
			hashtags.update(hashtags_in_tweet)
			

		taglist = []
		for tag in hashtags.most_common(15):
			taglist.append(tag)
		


	lineno=0
	for tag in taglist:
		print("{}:{}".format(lineno,tag))
		lineno+=1


	incidentMatrix = [[None for _ in range(len(taglist))] for _ in range(tweetnumber)]
	for i in range(tweetnumber):
		for j in range(len(taglist)):
			incidentMatrix[i][j]= 0
	

	tweetnumber = 0
	desiredrowindices = []
	desiredcolindices = []
	with open(fname,'r') as f:
		for line in f:
			tweet = json.loads(line)
			hashtags_in_tweet = get_hashtags(tweet)
			for hashTag in hashtags_in_tweet:
				try:
					index = [y[0] for y in taglist if y[1] >= 2].index(hashTag)
					incidentMatrix[tweetnumber][index] = 1
					desiredrowindices.append(tweetnumber)
					desiredcolindices.append(index)
				except:
					incidentMatrix[tweetnumber][index] = 0
			tweetnumber+=1

	desiredcolindices = set(desiredcolindices)
	desiredrowindices = set(desiredrowindices)
	zerolist = []
	for i in range(max(desiredcolindices)+1):
		zerolist.append(0)
	for lineno in desiredrowindices:
		templist = []
		for colno in desiredcolindices:
	 		templist.append(incidentMatrix[lineno][colno])
		if(templist != zerolist):
	 		print("{}:{}".format(lineno,templist))
