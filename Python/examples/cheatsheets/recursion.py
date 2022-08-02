# The process in which a function calls itself directly or indirectly is called recursion.
# Here is a Good example for Recursion in Python..
# This Recursion makes factorial-finding efficient compared to other methods using loops.

def factorial(n):
    if n < 0 :
        return 'try non-negative integer'
    elif n == 0 :
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input())
print(factorial(n))
