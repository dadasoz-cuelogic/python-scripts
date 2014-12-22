#!/usr/bin/python

#------------------------------------------------------------------------
str = "this is string example....wow!!!";

print "str.center(40, 'b') : ", str.center(40, 'b')

print '-'*50

#------------------------------------------------------------------------

str = "this is string example....wow!!!";

print "str.capitalize() : ", str.capitalize()

print '-'*50

#------------------------------------------------------------------------

str = "this is string example....wow!!!";

sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)
print '-'*50

#------------------------------------------------------------------------

str = "this is string example....wow!!!";
str = str.encode('base64','strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')
print '-'*50

#------------------------------------------------------------------------

print "Ends With"
str = "this is string example....wow!!!";

suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);

suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);
print '-'*50

#------------------------------------------------------------------------


str = "this is\tstring example....wow!!!";


print "Original string: " + str;
print "Defualt exapanded tab: " +  str.expandtabs();
print "Double exapanded tab: " +  str.expandtabs(16);
print '-'*50

#------------------------------------------------------------------------


str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

print '-'*50

#------------------------------------------------------------------------
