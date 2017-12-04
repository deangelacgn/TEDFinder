import pandas as pd
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize
from gensim.models import Doc2Vec
from sklearn.metrics.pairwise import cosine_similarity

ted_transcripts = pd.read_csv("data/transcripts.csv", encoding = 'utf-8')

def prepare_data(dataframe, field):
	for tag, row in enumerate(dataframe.loc[:, field]):
		yield TaggedDocument(words = normalize_text(row), tags = ['SENT_%s' % tag])

def normalize_text(sentence):
    sentence = sentence.lower()
    sentence = word_tokenize(sentence)
    return sentence

documents = prepare_data(ted_transcripts, 'transcript')

model = Doc2Vec(size = 128, window = 8, min_count = 0, workers = 4, alpha = 0.025, min_alpha = 0.025)

model.build_vocab(documents)

for e in documents:
 	print(e)

model.train(documents, total_examples = model.corpus_count, epochs = 1000)

ivec1 = model.infer_vector(normalize_text(" And our human nature isn't just selfish, it's also compassionate. It's not just competitive, it's also caring. Because of the depth of the crisis, I think we are at a moment of choice.The crisis is almost certainly deepening around us. It will be worse at the end of this year, quite possibly worse in a year's time than it is today. But this is one of those very rare moments when we have to choose whether we're just pedaling furiously to get back to where we were a year or two ago, and a very narrow idea of what the economy is for, or whether this is a moment to jump ahead, to reboot and to do some of the things we probably should have been doing anyway"), alpha = 0.1, min_alpha = 0.0001, steps = 10)

lista = []

for i in range(2466):
	lista.append((cosine_similarity(ivec1, model.docvecs['SENT_%s' % i]), i))

lista.sort(key=lambda x: x[0])

print(lista)
print(len(lista))
idx = lista[-1][1]

video  = ted_transcripts.loc[idx, 'url']
print(video)

print(lista[-1][1])


model.save('my_model.doc2vec')
