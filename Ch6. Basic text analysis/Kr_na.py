# -*- coding: utf-8 -*-

import networkx as nx
import itertools


def add_ties(g, sentence):

#각 문장에 대해서, 각 문장에서 함께 사용되는 단어들 사이에 관계 형성하기

	if len(sentence) > 0 :

		selected_words=list(g.nodes())
		
		for pair in list(itertools.combinations(set(sentence), 2)):
			if pair[0] == pair[1]:
				continue
			if pair[0] in selected_words and pair[1] in selected_words:
				if pair in list(g.edges()) or (pair[1],pair[0]) in list(g.edges()): 
					g[pair[0]][pair[1]]['weight'] += 1
				else:
					g.add_edge(pair[0], pair[1], weight=1 )
		return g
	else:
		return g


def form_network(g, sentences):
#원본 데이터와 가장 많이 출현하는 명사 단어 x개를 사용해서 그 단어들 사이의 관계 형성하기
    for sentence in sentences:
        g = add_ties(g, sentence)
        
    return g


def do_na(sentences, selected_words):
    G = nx.Graph()
    G.add_nodes_from(selected_words)
    G = form_network(G, sentences)
    
    return G