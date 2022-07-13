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


'''
Palindromes!
The first two examples will be iterative ways of determining whether a string is a palindrome.
The first one is less efficient than the next one.

I cannot believe I figured this one out.
'''

# ITERATIVE method 1

def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True 

# ITERATIVE method 2

def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True

# RECURSIVE adjusted for accepting upper case letters and spaces, but not punctuations?

def is_palindrome(my_string):
  my_string = my_string.strip(" ")
  my_string = my_string.lower()
  string_length = len(my_string)
  middle_index = string_length // 2
  if len(my_string) == 0:
    return True
  if my_string[0] == my_string[-1]:
    return is_palindrome(my_string[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)
print(is_palindrome("Level") == True)
print(is_palindrome("taco cat") == True)
print(is_palindrome("Was it a car or a cat I saw") == True)



'''
Multiplication substitute:
We're making a substitute for multiplication as if python didn't have the expression built in. 
'''

# ITERATIVE
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

# RECURSIVE 
def multiplication(num1, num2):
  if num1 == 0 or num2 == 0:
    return 0
  
  return num1 + multiplication(num1, num2 - 1)
# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)

'''
Binary Search Tree traversal with recurssion. 
'''


# ITERATIVE 

def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result
 
two_level_tree = {
"data": 6, 
"left_child":
  {"data": 2}
}
 
four_level_tree = {
"data": 54,
"right_child":
  {"data": 93,
   "left_child":
     {"data": 63,
      "left_child":
        {"data": 59}
      }
   }
}
 
 
depth(two_level_tree)
# 2
depth(four_level_tree)
# 4

# RECURSIVE 

def depth(tree):
  if not tree:
    return 0

  left_depth = depth(tree["left_child"])
  right_depth = depth(tree["right_child"])

  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1

# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)

