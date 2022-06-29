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


'''
Let us now depict the fibonacci sequence in both recursive and iterative fashion.
'''

# ITERATIVE
def fibonacci(n):
  list = [0,1]
  if n < 0:
    return ValueError("Input 0 or greater, please")
  elif n <= 1:
    return n
  else:
    while len(list) <= n:
      list.append((int(list[-2])) + (int(list[-1])))
      print(list)
  return list[n]

# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)

# RECURSIVE
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)
# test cases 
fibonacci(3)
fibonacci(7)
fibonacci(0)
