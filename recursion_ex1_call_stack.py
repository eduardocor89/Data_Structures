"""
Here I've created a call stack to visualize how recursion happens internally. 
By setting a key value pair inside a list, we can visualize how an interative
function would reach its base case by creating execution contexts to map 
the inner workings.

Following reaching the base case, I recursively add each value at the
top of the stack to the result
"""
def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while call_stack:
    return_value = call_stack[-1]
    call_stack.remove(return_value)
    print(call_stack)
    print("adding "+ str(return_value["n_value"]) +" to result")
    result += return_value["n_value"]
  return result, call_stack

sum_to_one(5)
