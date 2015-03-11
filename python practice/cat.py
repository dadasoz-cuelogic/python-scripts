def cat(filenames):
    for f in filenames:
        for line in open(f):
            print line,


cat(('abc.txt','file.py','extcount.py'))