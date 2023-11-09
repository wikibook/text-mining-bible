# -*- coding: utf-8 -*-


import nltk
import networkx as nx
import itertools
from collections import Counter
import re

def get_words_list(counter_list):
    words = []
    for word, count in counter_list:
        words.append(word)
    return words


def get_sentences(text):
    sentences = re.split(r'[\.\?\!]\s+', text)
    return sentences

def add_ties(g, sentence, words_list):

#각 문장에 대해서, 각 문장에서 함께 사용되는 단어들 사이에 관계 형성하기

    selected_words = []    
    word_tokens = nltk.word_tokenize(sentence)
    tokens_pos = nltk.pos_tag(word_tokens)
    NN_words = []
    for word, pos in tokens_pos:
        if 'NN' in pos:
            NN_words.append(word)
			
    wlem = nltk.WordNetLemmatizer()
    lemmatized_words = []
    for word in NN_words:
		#print(word, pos)
        new_word = wlem.lemmatize(word)
		#print('lemma: ', new_word)
        lemmatized_words.append(new_word)
    
    for word in lemmatized_words:
        if word in words_list:
            selected_words.append(word)
    
    selected_words = set(selected_words)

    for pair in list(itertools.combinations(list(selected_words), 2)):
        if pair[0] == pair[1]:
            continue
        if pair in list(g.edges()) or (pair[1],pair[0]) in list(g.edges()): 
            g[pair[0]][pair[1]]['weight'] += 1
            
        else:
            g.add_edge(pair[0], pair[1], weight=1 )
    
    return g


def form_network(g, article, words_list):
#원본 데이터와 가장 많이 출현하는 명사 단어 x개를 사용해서 그 단어들 사이의 관계 형성하기
    for sentence in article:
        sentence = sentence.lower()
        g = add_ties(g, sentence, words_list)
        
    return g

def do_na(filtered_content, selected_words):
	# 선택되어진 단어를 사용자로부터 입력 받는다.
	# 원본 텍스트 데이터를 문장으로 쪼개기
	# in order to find ties between words, we first need to split the article content into sentences
	article_sentences = get_sentences(filtered_content)
	#print(article_sentences)

	# 가장 많이 출현하는 10개의 명사 단어들에 대해서 네트워크 생성하기
	# Using the 10 words, we create a network
	G = nx.Graph()
	G.add_nodes_from(selected_words)
	G = form_network(G, article_sentences, selected_words)
	return G
