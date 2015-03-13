def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(lines):
    return (line for line in lines if len(line) > 40)

def printlines(lines):
    for line in lines:
        print line,

def main(filenames):
	lines = readfiles(filenames)
	lines = grep(lines)
	printlines(lines)

f = ["prob58.py","prob59.py"]
main(f)