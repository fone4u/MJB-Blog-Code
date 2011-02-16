'''
@author Michael J Bommarito II
@date Feb 16, 2011
'''

import codecs
import dateutil.parser
import nltk

def readTweets(fileName):
	'''
	Read in the tweet data.  This is just tab-delimited.
	'''
	rows = [[field.strip() for field in line.split("\t")] for line in codecs.open(fileName, 'r', 'utf-8')]
	return [(int(row[0]), dateutil.parser.parse(row[1]), row[2], row[3]) for row in rows]

def main():
	'''
	Main
	'''
	porter = nltk.PorterStemmer()
	tweets = readTweets("data/tweets_25bahman.csv")
	minLength = 3
	
	corpus = [nltk.Text([porter.stem(w.lower()) for w in nltk.word_tokenize(tweet[3]) if len(w) >= minLength]) for tweet in tweets]		
	print corpus[0]
	
if __name__ == "__main__":
	main()