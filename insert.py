import argparse
import itertools
import collections
import pandas as pd
import psycopg

filename = "tweets.txt"
conn = psycopg.connect("dbname=tweets")

def insert_data(time, time_group, phrase):
	list1 = [time, time_group, phrase]
	cur = conn.cursor()
	
	query = """
	
	INSERT INTO tweets(time_stamp, time_group, word_or_phrase)
	VALUES (%s, %t, %s);

	"""
	cur.execute(query, list1)
	conn.commit()	
	cur.close()
	
	list1 = []
		
def main():
	 #break down into phrases
	with open(filename, "r") as files:
		for line in files:
			line_l = line.split(",")
			time = line_l[0]
			word_ls = line_l[1]
			
			word_num = word_ls.split()
			
			for i in range(len(word_num)):
				if i == len(word_num) - 1:
					pass
				else:
					phrase = word_num[i] + " " + word_num[i+1]
					time_group = '2021-11-30 09:31:00'
					insert_data(time, time_group, phrase)
	               
	

	
	#cur.execute(query_1)
	
	#query_2 = """
	
	#select * from tweets;

	#"""
	
	#cur.execute(query_2)
	
	#for row in cur:
		#print(row)
		

	
	print("successed")
	

if __name__ == '__main__':
	main()

					
