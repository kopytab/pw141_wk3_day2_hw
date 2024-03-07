# Fizz Buzz 
# Given a random number as an input to a function, return "FIZZ" if the number is even and "BUZZ" if the number is odd

# create a function fizz_buzz


def fizz_buzz(num):
    if num % 2 == 0:
        return "Fizz"
    else:
        return "Buzz"
    
# print(fizz_buzz(12))

# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print 'Fizz' instead of the number
# If the number is divisible 5, print 'Buzz' instead of the number
# If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# Otherwise, simply print the number


def fizz_buzz2(numbers):
    for num in range(1, numbers + 1):

        

        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else:
            print(num)


fizz_buzz2(15)