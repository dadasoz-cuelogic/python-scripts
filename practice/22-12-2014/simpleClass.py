def as_number(n,class_=int):
    return class_(n)

print as_number("3.14",str)

print as_number("3.14", float)