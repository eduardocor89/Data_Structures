"""
Here I'll demonstrate recursive and non recursive ways of solving the same problem.
It's elementary but fundamental....WATSON!
"""

# ITERATIVE
def factorial(n):
  if n <= 1:
    return 1
  result = n
  for i in range(n-1,0,-1):
    result *= i
  return result 

# RECURSIVE

def factorial(n):  
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)
