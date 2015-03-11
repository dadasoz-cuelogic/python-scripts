class Reversed:
    def __init__(self, seq):
        self.seq = seq
    def __len__(self):
        return len(self.seq)
    def __getitem__(self, i):
        return self.seq[-(i + 1)]

#for x in Reversed(sequence):
   # print x # do something with x