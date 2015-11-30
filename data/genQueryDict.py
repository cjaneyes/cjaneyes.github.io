import os, sys

def readQueryDictionary(queryFilePath):
	query = open(queryFilePath, 'r')
	dict = {}
	for line in query:
		parse = line.strip().split(" ")
		for i in range(1, len(parse)):
			if dict.has_key(parse[i]):
				continue
			dict[parse[i]] = [0, 0, False]
	return dict

def writeTermInfo(termFilePath):
	output = open(termFilePath, 'w')

#if __name__ == "__main__":
#	print readQueryDictionary("/bos/usr0/jingc1/dbpedia/INEX-LD")