# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
import re

def En_preprocessing(text, customized_stopwords):
# 1. 불필요한 symbols과 marks 제거하기
	filtered_content1 = re.sub(r'[^\.\?\!\s\d\w]','',text)
	filtered_content1 = filtered_content1.replace('Mr.', 'Mr').replace('Dr.', 'Dr')
	filtered_content2 = re.sub(r'[^\s\d\w]','',filtered_content1)
# 2. Case conversion; 대문자를 소문자로 바꾸기
	filtered_content2 = filtered_content2.lower()

# 3. Word tokenization
	word_tokens = nltk.word_tokenize(filtered_content2)

# 4. POS tagging
	tokens_pos = nltk.pos_tag(word_tokens)

# 5. Select Noun words
	NN_words = []
	for word, pos in tokens_pos:
		if 'NN' in pos:
			NN_words.append(word)

# 6. Lemmatization
# nltk에서 제공되는 WordNetLemmatizer을 이용하는 경우 
	wlem = nltk.WordNetLemmatizer()
	lemmatized_words = []
	for word in NN_words:
		#print(word, pos)
		new_word = wlem.lemmatize(word)
		#print('lemma: ', new_word)
		lemmatized_words.append(new_word)

# 7. Stopwords removal
# 1차적으로 nltk에서 제공하는 불용어사전을 이용해서 불용어를 제거할 수 있습니다.

	stopwords_list = stopwords.words('english') #nltk에서 제공하는 불용어사전 이용
	#print('stopwords: ', stopwords_list)
	unique_NN_words = set(lemmatized_words)
	final_NN_words = lemmatized_words

	for word in unique_NN_words:
		if word in stopwords_list:
			while word in final_NN_words: final_NN_words.remove(word)
				

#------------------------------------------------
# 제거하거자 하는 단어가 nltk에서 제공되는 사전에 포함되어 있지 않은 경우에, 아래와 같이 직접 만들어 사용할 수도 있습니다.
	unique_NN_words1 = set(final_NN_words)
	for word in unique_NN_words1:
		if word in customized_stopwords:
			while word in final_NN_words: final_NN_words.remove(word)
#------------------------------------------------

	return filtered_content1, final_NN_words
