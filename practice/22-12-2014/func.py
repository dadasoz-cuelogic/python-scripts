def test():
    print "xx"
    print "xxxx"

test()

def printinfo( name, age = 35,mobile=9970420742 ):
    "This prints a passed info into this function"
    print "Name: ", name;
    print "Age ", age;
    print "Mobile ", mobile;
    list=[name,age,mobile]
    return list;

# Now you can call printinfo function
printinfo( age=50, name="miki" );
printinfo( name="miki" );
printinfo( 24,"Nishant",878585885 );
print printinfo( "Nishant",878585885,24 );