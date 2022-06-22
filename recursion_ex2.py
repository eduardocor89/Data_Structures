'''
Start simple:
Let's use recursion to add to one.
Our base case is laid out first, with our recursive step second.

Remember, we're trying to reach the base case whence we can derive our
answer
'''

# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return 1
  else:
    print("Recursing with input: {0}".format(n))
    return sum_to_one(n - 1) + n

print(sum_to_one(7))
