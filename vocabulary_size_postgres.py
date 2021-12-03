"""
File: word_count_postgres.py
Name: Group
---------------------------
This file calculate the vocabulary size in the current minute. The user need to input a time and will return the vocabulary size.
"""

import argparse
import itertools
import collections
import pandas as pd
import psycopg
import datetime

conn = psycopg.connect("dbname=tweets")

def cal_vocabulary_size(time):
	"""
	calculate the vocabulary sizein the current minute
	"""
	# write your psycopg query here fighting :) 
	# the input time will be "timestamp"
	# so look like below
	# query = """
	#	select * from table where time_stamp == {time}
	# 
	# 	"
	cur = conn.cursor()
	
	query = """
	
	select time_stamp, time_group, word, word_count 
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
	
	WORD_DICT = {}
	timestamp = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
	timegroup = timestamp + datetime.timedelta(seconds = -timestamp.second)
	print("Current Time Group:" , timegroup)

	for i in res:
		if i[1] == timegroup and i[2] not in WORD_DICT:
			#vocabulary_size += 1
			WORD_DICT[i[2]] = 1   
		else:
			pass
	
	print('The Vocabulary Size in Current Time Group is', len(WORD_DICT))

	#pass



def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('---timestamp', type=str, help='enter your word -timestamp "time"')
	args = parser.parse_args()
	
	time = args.timestamp
	
	cal_vocabulary_size(time)


        
if __name__ == '__main__':
	main()	



