import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def read_data(path):
	ted_data = pd.read_csv(path)
	return ted_data

def tf_idf(keys, dataframe, label, min_videos=1):
	tfidf_vectorizer = TfidfVectorizer()
	tfidf_matrix = tfidf_vectorizer.fit_transform(dataframe.loc[:, label])

	query = tfidf_vectorizer.transform([keys])
	cs = cosine_similarity(query, tfidf_matrix)
	similarity_list = cs[0]
	result_list = []
	while min_videos > 0:
		tmp_index = np.argmax(similarity_list)
		result_list.append(tmp_index)
		similarity_list[tmp_index] = 0
		min_videos -= 1

	print("result_list: %s"%result_list)
	return result_list

#tfidf_vectorizer = TfidfVectorizer()
#tfidf_matrix = tfidf_vectorizer.fit_transform(documents)


# a = read_data("/Users/rqroz/Desktop/GITHUB/doc2vec-tensorflow/doc2vec/website/static")
# video_id = tf_idf("capitalism", a, 'transcript')
#
# print(a.loc[video_id, 'url'])
