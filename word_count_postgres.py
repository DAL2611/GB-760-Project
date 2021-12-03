"""
File: word_count_postgres.py
Name: Group
---------------------------
This file compute frequencies of words and phrases 
by using psycopg. The user will input a word and will
return the frequency of that word.
"""

import argparse
import itertools
import collections
import pandas as pd
import psycopg
import datetime

conn = psycopg.connect("dbname=tweets")

def count_freq_word(word, time):
	"""
	count the frequency of that word in the current minute
	"""
	# write your psycopg query here fighting :) 
	# the input word will be "word"
	# so look like below
	# query = """
	#	select * from table where word == {word}
	# 
	# 	"
	cur = conn.cursor()
	
	query = """
	
	select time_stamp, time_group, word_or_phrase, count 
	from tweets
	limit 20;
	"""
	
	cur.execute(query)
	res = []
	#keys = {"time_stamp","time_group", "word_or_phrase", "count"}
	#keys = {"count", "time_stamp", "word_or_phrase", "time_group"}
	#value = {1,2,3,4}
	#res = dict(zip(keys, value))
	for row in cur:
		#dic = dict(zip(keys, row))
		row = list(row)
		res.append(row)
	
	conn.commit()	
	cur.close()
	
	count = 0
    #word_dict = {}
	timestamp = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
	timegroup = timestamp + datetime.timedelta(seconds = -timestamp.second)
	print("Current Time Group:" , timegroup)

	for i in res:
		if i[2] == word and i[1] == timegroup:
			count = count + i[3]
	print(count)
	
	pass



def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-w','--word', type=str, help='enter your word -w word and phrase -w "phrase" ')
	parser.add_argument('---timestamp', type=str, help='enter your word -timestamp "time"')
	args = parser.parse_args()
	
	word = args.word
	time = args.timestamp
	
	print(word)
	count_freq_word(word, time)     



        
if __name__ == '__main__':
	main()	



