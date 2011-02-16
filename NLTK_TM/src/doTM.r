#@author Michael J Bommarito II
#@date Feb 16, 2011

library(tm)

# Load the tweets
tweets <- unique(read.table('data/tweets_25bahman.csv', sep="\t", quote="", comment.char="", header=FALSE, nrows=100000, stringsAsFactors=FALSE))
names(tweets) <- c("id", "date", "user", "text")

# Build the corpus and then apply the tm pre-processing methods
corpus <- Corpus(VectorSource(tweets$text))
corpus <- tm_map(tm_map(tm_map(corpus, stripWhitespace), tolower), stemDocument)
