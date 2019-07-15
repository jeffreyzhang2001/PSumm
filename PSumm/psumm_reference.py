from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from heapq import nlargest

"""
1. Pass original_text into main function as argument
2. Remove stopwords by calling remove_stopwords(original_text)
2. Tokenize no_stopwords_text into list of words --> word_list
3. Construct dictionary that acts as frequency table: word_freq_table (key:value = word:length)
3. For loop a dictionary by looping through list
    a. Count length of sentence --> temp_sentence_len
    b. Remove stopwords from sent_tokenized_text[x]
    c. Store stopword removed text in dictionary (key) and assign value (length)
#Extractive techniques
#1. Rank sentences by dividing each word's frequency by most frequent occuring word (BETTER FOR CONCISE TEXTS, LONGER SENTENCES HAVE AN ADVANTAGE)
#2. Rank sentences by dividing each word's frequency by sentence length (BETTER FOR VERBOSE TEXTS, AS LONGER SENTENCES DON'T HAVE AN ADVANTAGE)
"""

#Cache stopwords in set to improve lookup time
stop_words = set(stopwords.words('english'))
stop_words.update(["’", ",", "—"])

#Function removes stopwords according to nltk's stopword list
def remove_stopwords(original_text):
    no_stopwords_text = ' '.join([word for word in word_tokenize(original_text.lower()) if word not in stop_words])
    return no_stopwords_text

#Function calculates sentence importance score
#EXTRACTIVE TECHNIQUE 1: Takes into consideration verbosity (sentence length)
def score_sentence_considering_verbosity(sent_tokenized_no_stopword_text, x):
    temp_word_tokenized_list = word_tokenize(sent_tokenized_no_stopword_text[x])
    sentence_score = 0
    for x in range(len(temp_word_tokenized_list)):
        if temp_word_tokenized_list[x] not in stop_words and temp_word_tokenized_list[x] != ("." or "?"):
            sentence_score += word_freq_table[temp_word_tokenized_list[x]]
    #Sentence score is DIVIDED by number of 'useful' words in sentence
    sentence_score /= len(temp_word_tokenized_list)
    return sentence_score 

#EXTRACTIVE TECHNIQUE 2: Takes into consideration relative frequency, but prefers longer sentences
def score_sentence_considering_relative_frequency(sent_tokenized_no_stopword_text, x):
    temp_word_tokenized_list = word_tokenize(sent_tokenized_no_stopword_text[x])
    sentence_score = 0
    for x in range(len(temp_word_tokenized_list)):
        if temp_word_tokenized_list[x] not in stop_words and temp_word_tokenized_list[x] != ".":
            sentence_score += word_freq_table[temp_word_tokenized_list[x]]
    sentence_score /= (max(word_freq_table.values()))
    return sentence_score 

#Tokenizes no_stopwords_text into words
word_list = word_tokenize(remove_stopwords(original_text))
#Creates dictionary that functions as frequency table
word_freq_table = {}

#Loops through word_list and creates new entry in word_freq_table if
#one doesn't already exist and adds a tally if entry already exists 
for w in word_list:
    if w not in word_freq_table and w != ".":
        word_freq_table[w] = 1

    elif w in word_freq_table:
        word_freq_table[w] += 1

#Tokenize original text
sent_tokenized_original_text = sent_tokenize(original_text)
sent_tokenized_no_stopword_text = sent_tokenize(remove_stopwords(original_text))

#Initialize empty dictionaries to plug INDEX of sentence scored by function into original_tokenized_sentencesassociate (key) with its sentence_score (value)
scored_sentences_dictionary_verbosity = {}
scored_sentences_dictionary_relative_frequency = {}

#Loop through no_stopword_text and runs each sentence through score_sentence(), and passes the equivalent original sentence into a dictionary with the sentence_score as the value
for x in range(len(sent_tokenized_no_stopword_text)):
    scored_sentences_dictionary_verbosity[sent_tokenized_original_text[x]] = score_sentence_considering_verbosity(sent_tokenized_no_stopword_text, x)
    scored_sentences_dictionary_relative_frequency[sent_tokenized_original_text[x]] = score_sentence_considering_relative_frequency(sent_tokenized_no_stopword_text, x)
    
#Sort dictionaries by descending sentence score and output N highest scoring sentences
def summarize():
    return(nlargest(3, scored_sentences_dictionary_verbosity,key=scored_sentences_dictionary_verbosity.get))
    return(nlargest(3, scored_sentences_dictionary_relative_frequency, key=scored_sentences_dictionary_verbosity.get))

def main(original_text):
    remove_stopwords(original_text)
    summarize()

if __name__ == '__main__':
    main(original_text)