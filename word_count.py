"""
This file compute frequencies of words and phrases 
by using argparse
"""

import argparse

# create args
parser = argparse.ArgumentParser()
parser.add_argument('word', metavar='word', type=str, help='enter your word')
args = parser.parse_args()

word = args.word

print(word)
