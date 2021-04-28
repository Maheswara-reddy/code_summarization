import bs4 as bs
import numpy
import re
import nltk
import heapq

# reading the containing the setences from the source code.
scraped_data = open("myfile.txt", "r")
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

# read paras from the text file.
paragraphs = parsed_article.find_all('p')

# perform operations on this string.
article_text = ""

for p in paragraphs:
    article_text += p.text

# Removing square brackets and extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# sentence tokenization.
sentence_list = nltk.sent_tokenize(article_text)

# store all english stop words in stopwords.
stopwords = nltk.corpus.stopwords.words('english')

# Dictionary - words & their frequencies.
word_frequencies = {}

# variable to find the frequncy of sentences.
for word in nltk.word_tokenize(formatted_article_text):

    # if the word is not a stopword.
    if word not in stopwords:

        # if words are encountered for the first time, add to the list.
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        
        # if words are present, increase the frequency.
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

# weighted frequencies.
for word in word_frequencies.keys():

    # weighted frequencies.
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

# Dictionary - sentences & their scores.
sentence_scores = {}

for sent in sentence_list:

    # tokenize the sentences.
    for word in nltk.word_tokenize(sent.lower()):

        # for all word in dictionary.
        if word in word_frequencies.keys():

            # only sentences less than 30 words are claculated.
            if len(sent.split(' ')) < 30:

                # if new sentence - add to the dictionary.
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]

                # old sentences - increase score.
                else:
                    sentence_scores[sent] += word_frequencies[word]


# generate summary.
# return 12 sentences with highest score.
summary_sentences = heapq.nlargest(12, sentence_scores, key=sentence_scores.get)

#  jpin the sentences.
summary = ' '.join(summary_sentences)
print(summary)
