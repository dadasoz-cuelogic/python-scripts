def readfiles(filenames):
	for f in filenames:
		for line in open(f):
			yield line

def checkline(lines):
	return [line for line in lines if len(line)>40]



def main(filenames):
	lines=readfiles(filenames)
	print checkline(lines)

main(('data.txt','abc.txt'))