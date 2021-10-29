"""
This file compute frequencies of words and phrases 
by using argparse
"""

import argparse

words = []
count = 0

with open ("tweet4.txt","r") as f: 
    # Get a list of lines in the file and covert it into a set 
    words = set(f.readlines()) 
    count = len(words) 

print(count)

