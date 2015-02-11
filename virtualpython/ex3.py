"""In this exercise, you will need to add numbers and 
strings to the correct lists using the "append" list method.
You must add the numbers 1,2, and 3 to the "numbers" list, and
the words 'hello' and 'world' to the strings variable."""

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('Hello')
strings.append('World')
second_name = names[1]

print("Numbers List:%r"%numbers)
print("String list:%s"% strings)
print("The second name on names list is %s"%second_name)


