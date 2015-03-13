class rev_iter:
    def __init__(self, n):
        self.n = n
        self.i = len(n) - 1

    #def __iter__(self):
     #   return self

    def next(self):
            if self.i >= 0:
                print self.n[self.i]
                self.i -= 1
            else:
                raise StopIteration

z = rev_iter([1,2,3,4])
z.next()
z.next()
z.next()
z.next()
z.next()
