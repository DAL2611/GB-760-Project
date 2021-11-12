
"""
File: word_count.py
Name: Group
---------------------------
This file compute frequencies of words and phrases 
by using argparse
"""

import argparse
import itertools
import collections

FILENAME = 'tweets.txt'
WORD_DICT = {}


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



def read_file(filename, word):
	"""
	Read the file 
	"""
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			line_l = line.split(",")
			count_freq_word(line_l)

def main():
	# create args
	parser = argparse.ArgumentParser()
	# parser.add_argument('word', metavar='word', type=str, help='enter your word')
	# parser.add_argument('sentence', help='enter your sentence')
	parser.add_argument('-w','--word', help='enter your word', required=False)
	args = parser.parse_args()
	
	word = args.word
	
	read_file(FILENAME, word)
	print(WORD_DICT[word])

if __name__ == '__main__':
	main()	

