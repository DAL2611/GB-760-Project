
"""
File: server_postgres.py
Name: Group
---------------------------
This file compute frequencies of words and phrases 
by using argparse and add them up into a `
"""

import argparse
import itertools
import collections
import pandas as pd
# ngram

FILENAME = 'tweets.txt'
WORD_DICT = {}

#def tell_time_grorup(line):
	#time_stamp = line[1].split(" ") 
	#for time in time_stamp:
		

def count_freq_word(line):
	"""
	Count the frequency of the words
	"""
	word_ls = line[1].split(" ")  
	for word in word_ls:

		if word not in WORD_DICT:
			if '@' in word:
				pass
			else:
				WORD_DICT[word] = 1   
		else:
			WORD_DICT[word] += 1


def read_file(filename, word, mode='Word'):
	"""
	Read the file and count phrase frequency
	"""
	with open(filename, 'r') as f:
		count = 0
		for line in f:
			line = line.strip()

			# count frequency of phrase or word 
			if mode == 'Phrase':
				if word in line:
					count += 1
			if mode == 'Word':
				line_l = line.split(",")
				count_freq_word(line_l)

		if mode == 'Phrase':
			return count

'''
def get_word():
	with open('tweets.txt','r') as file:
		# reading each line    
		for line in file:
			# reading each word        
			for word in line.split():
				if '@' in word:
					continue
				if ',' in word:
					continue
				else:
					print(word) 
'''
'''
#import re
word_list = get_word()
print(type(word_list))
#word_list = re.sub(r'[^a-z]', '', word_list)
#array_length = len(word_list)
'''

word_list = ['text', 'know', 'think', 'person']
array_length = len(word_list)

def main():
	#for i in word_list:
	for i in range(array_length):
		# create args
		parser = argparse.ArgumentParser()
		parser.add_argument('-w','--word', help='enter your word -w word and phrase -w "phrase" ',
							required=False, default=word_list[i])
		args = parser.parse_args()
		word = args.word
		
		# identify whether this is a phrase or word
		phrase = word.split(" ")
		if len(phrase) > 1:
			# if phrase
			count = read_file(FILENAME, word, mode='Phrase')
			print(word, count)
		else:
			# if word
			WORD_DICT[word] = 0
			read_file(FILENAME, word, mode='Word')
			print(word, WORD_DICT[word])
			
	#table = pd.DataFrame(WORD_DICT.items())		
	#print(table)
			

if __name__ == '__main__':
	main()



