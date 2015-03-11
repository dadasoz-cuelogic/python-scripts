She sells seashells on the seashore;
The shells that she sells are seashells Im sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.
Problem 18: Write a program to print each line of a file in reverse order.
Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
Head Command Examples in Unix / Linux Tutorials
The head command in unix or linux system is used to print the first N lines from the file to the terminal. The syntax of head command is 
head [options] [files]
The head command options are: 
c : Prints the first N bytes of file; With leading -, prints all but the last N bytes of the file.
n : Prints first N lines; With leading - print all but the last N lines of each file.
Head Command Examples: 
Create the following file in your linux or unix operating system for practicing the examples: 
> cat example.txtfedora
1. Display first 10 lines 
By default, the head command prints the first 10 lines from a file. 
head example.txt
.Display first N lines 
Use the -n option to print the first n lines from a file. The following example prints the first 2 lines from the file: 
> head -n2 example.txt
linux storage
ubuntu os
3. Skip last N lines 
You can skip the last N lines from a file and print the remaining lines. The following example skips the last 2 lines and prints the remaining lines. 
> head -n-2 example.txt
linux storage
4. Print the first n bytes. 
use the -c option to print the first N bytes from the file. The following example prints the first 5 bytes from the file. 
