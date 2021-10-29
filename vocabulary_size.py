"""
This file compute and print the number of unique words
used in all the tweets stored in tweets.txt
"""


filename = 'tweet4.txt'

WORD_DICT = {}

def count_freq_word(line):
	
	word_ls = line[1].split(" ")
	# print(word_ls)
	for word in word_ls:
		if word not in WORD_DICT:
			WORD_DICT[word] = 1
		else:
			pass


def main():
	with open(filename, 'r') as f:
		for line in f:
			if "text" in line:
				line_l = line.split(':')
				count_freq_word(line_l)

				# print(line_l)

	print(len(WORD_DICT))


if __name__ == '__main__':
    main()
