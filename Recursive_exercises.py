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

'''
Let us now write an recursive algorithm to sum the digits of a number.
For example if sum_digits(12) it would return 3 since 1 + 2 is 3.
'''

# ITERATIVE
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

# test cases
sum_digits(12)
sum_digits(552)
sum_digits(123456789)

# RECURSIVE

def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit
  
# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)


'''
Let us now write an algorithm that finds the smallest (even negative) value of a list.
For example: [1,2,3,4,-1,6,7,8]
'''

# ITERATIVE
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min
 
find_min([42, 17, 2, -1, 67])
# -1
find_mind([])
# None
find_min([13, 72, 19, 5, 86])
# 5

# RECURSIVE
def find_min(my_list, min=None):
  if len(my_list) == 0:
    return min
  else:
    if min == None or my_list[0] < min:
      min = my_list[0]
  return find_min(my_list[1:], min)
   
# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)

