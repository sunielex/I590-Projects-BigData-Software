#!/usr/bin/python

#function fizzbuzz
def fizzbuzz(n):
    if n % 2 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    elif n % 2 == 0:
        return 'Fizz'
    elif n % 3 == 0:
        return 'Buzz'
    else:
        return str(n)


#take input from the user
user_input = input("Enter a valid +ive number: ")

#Iterate and Print corresponding value
for n in range(1, user_input+1):
        print fizzbuzz(n)
