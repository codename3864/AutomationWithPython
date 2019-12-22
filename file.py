import sys 

def cat(filename):
	f = open(filename,'r')
	for line in f:
		print(line)
cat(filename.text)
