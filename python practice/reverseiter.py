class yrange:
    def __init__(self,n):
        self.i =n 
        self.n = 0

   # def __iter__(self):
     #   return self

    def next(self):
        if self.i >= self.n:
            i = self.i
            self.i -= 1
            return i
        else:
            raise StopIteration()


y=yrange(5)
print y.next()
print y.next()
print y.next()
print y.next() 
print y.next() 