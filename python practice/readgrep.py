def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern,lines):
     	for line in lines:
            if pattern in line:
                return line,

def printlines(lines):
    for line in lines:
        print line,

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

main('Enter',('abc.txt','add.py'))