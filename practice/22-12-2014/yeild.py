def test():
    yield "xx"
    yield "yy"
    yield "zz"
    yield "bb"
l=list(test())
print l