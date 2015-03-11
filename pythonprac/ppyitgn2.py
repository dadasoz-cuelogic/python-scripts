import sys

def printlines(name, width):
    with open(name) as f:
        return [line for line in f if len(line) > width]


def mainfunc():
    if len(sys.argv) != 2:
        print 'Usage: python {0} filename'.format(sys.argv[0])
        sys.exit(1)

    for line in printlines(sys.argv[1], 40):
        print line,


if __name__ == '__main__':
    mainfunc()