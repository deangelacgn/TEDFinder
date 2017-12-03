import pandas as pd
import math
import string
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

"""
document_0 = "I'm often asked, What surprised you about the book? And I say, That I got to write it. I would have never imagined that. Not in my wildest dreams did I think  I don't even consider myself to be an author."
document_1 = "I'd like to talk today about the two biggest social trends in the coming century, and perhaps in the next 10,000 years. But I want to start with my work on romantic love, because that's my most recent work. "
document_2 = " I started out by trying to figure out what romantic love was by looking at the last 45 years of the psychological research and as it turns out, there's a very specific group of things that happen when you fall in love."
document_3 = "On September 10, the morning of my seventh birthday, I came downstairs to the kitchen, where my mother was washing the dishes and my father was reading the paper or something, and I sort of presented myself to them in the doorway."

all_documents = [document_0, document_1, document_2, document_3]
"""
def tokenize(text_document):
	return text_document.lower().split(" ")
 
def term_frequency(word, document):
    return document.count(word)
 
def sublin_term_frequency(word, document):
    count = document.count(word)
    if count == 0:
        return 0
    return 1 + math.log(count)

def docs_contain_token(word, list_of_documents):
	counter = 0
	for document in list_of_documents:
		if word in document:
			counter+=1

	return counter
 
def inverse_document_frequencies(documents):
    idf_values = {}
    #print("passo 1")
    all_tokens_set = set([item for sublist in documents for item in sublist])
    #print("passo 2")
    for tkn in all_tokens_set:
        contains_token = docs_contain_token(tkn, documents)
        idf_values[tkn] = 1 + math.log(len(documents)/(contains_token))
    return idf_values
 
def tfidf(documents):
    #print("1")
    documents = [tokenize(d) for d in documents]
    #print("2") 
    idf = inverse_document_frequencies(documents)
    tfidf_documents = []
    #print("3")
    for document in documents:
        doc_tfidf = []
        for term in idf.keys():
            tf = sublin_term_frequency(term, document)
            doc_tfidf.append(tf * idf[term])
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents

def cos_similarity(vector1, vector2):
    dot_product = sum(p*q for p,q in zip(vector1, vector2))
    magnitude = math.sqrt(sum([val**2 for val in vector1])) * math.sqrt(sum([val**2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product/magnitude

"""
sklearn_tfidf = TfidfVectorizer(norm = 'l2',min_df = 0, use_idf = True, smooth_idf = False, sublinear_tf = True, tokenizer = tokenize)
sklearn_tfidf_docs = sklearn_tfidf.fit_transform(all_documents)

raw_tfidf_docs = tfidf(all_documents)

tfidf_raw_comparisons = []

for count_0, doc_0 in enumerate(raw_tfidf_docs):
    for count_1, doc_1 in enumerate(raw_tfidf_docs):
        tfidf_raw_comparisons.append((cos_similarity(doc_0, doc_1), count_0, count_1))

tfidf_sklearn_comparisons = []

for count_0, doc_0 in enumerate(sklearn_tfidf_docs.toarray()):
    for count_1, doc_1 in enumerate(sklearn_tfidf_docs.toarray()):
        tfidf_sklearn_comparisons.append((cos_similarity(doc_0, doc_1), count_0, count_1))

for x in zip(sorted(tfidf_raw_comparisons, reverse = True), sorted(tfidf_sklearn_comparisons, reverse = True)):
    print(x)
"""

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

def read_data(path, label):
    data = pd.read_csv(path)
    list_of_docs = data.loc[:, label].tolist()
    list_of_docs = [ doc.lower().translate(str.maketrans('','',string.punctuation)) for doc in list_of_docs]       

    return data, list_of_docs

def tf_idf(data):

    tfidf_vectorizer = TfidfVectorizer(stop_words = 'english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data)
    print(tfidf_matrix)

    return tfidf_vectorizer, tfidf_matrix

def most_similar(keys, vectorizer, tfidf_matrix):
    query = vectorizer.transform([keys])
    cs = cosine_similarity(query, tfidf_matrix)
    print(max(cs[0]))
    return np.argmax(cs[0])

"""
a, b = read_data("/Users/deangelaneves/Trabalho final IA/data/transcripts.csv", 'transcript')
vec, matrix = tf_idf(b)
video_id = most_similar("i love capitalism", vec, matrix)
print(a.loc[video_id, 'url'])

#tfidf_vectorizer = TfidfVectorizer()
#tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
"""

# a = read_data("/Users/rqroz/Desktop/GITHUB/doc2vec-tensorflow/doc2vec/website/static")
# video_id = tf_idf("capitalism", a, 'transcript')
#
# print(a.loc[video_id, 'url'])


