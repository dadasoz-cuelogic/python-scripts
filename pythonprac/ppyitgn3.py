'''def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print line

grep('a',('a.txt',))'''

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in lines)

def printlines(lines):
    for line in lines:
        print line,

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)


readfiles(('a.txt', 'interpreter.txt'))
#grep('!', ('a.txt', 'interpreter.txt'))
#printlines(('a.txt', 'interpreter.txt'))
#main('!', ('a.txt, interpreter.txt'))