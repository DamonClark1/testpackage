def sum_array(array):
    '''Return sum of all items in array'''

    total = 0
    for element in array:
        if type(element) == type([]):
            total = total + sum_array(element)
        else:
            total = total + element

    return total

def fibonacci(n):
    '''Return nth term in fibonacci sequence'''

    if n+1 < 0:
        print("Incorrect input, please make sure the number is > 0")
    elif n+1 == 1:
        return 0
    elif n+1 == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    '''Return n!'''

    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    '''Return word in reverse'''

    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
