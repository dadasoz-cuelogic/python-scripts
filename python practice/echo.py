def min(list):
     min=list[0]
     for i in list:
             for j=i-1 in list:
                     if(list[i]<=list[j]):
                             min=list[i]
                     else:
                             min=list[j]
     return min
Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
The head command in unix or linux system is used to print the first N lines from the file to the terminal. The syntax of head command is 
head [options] [files]
The head command options are: 
By default, the head command prints the first 10 lines from a file. 
> head example.txt
> head -n2 example.txt
> head -n-2 example.txt
> head -c5 example.txt
Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
The head command in unix or linux system is used to print the first N lines from the file to the terminal. The syntax of head command is 
head [options] [files]
The head command options are: 
By default, the head command prints the first 10 lines from a file. 
head example.txt
> head -n2 example.txt
> head -n-2 example.txt
> head -c5 example.txt
