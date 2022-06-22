"""
Let's use recursion to remove nested lists within a list
but keeps the values contained (and not spelled out like t h i s, 
which happens when you try to flatten lists with nested for loops.

Our base case is the lack of a list so I'm gonna use isistnace() to
determine wether each element is an instance of a list. If it isn't a list
then I iterate through until I find no more lists. 
"""

def flatten(my_list):
  result = []
  for element in my_list:
    if isinstance(element,list):
      print("List found!")
      flat_list = flatten(element)
      result += flat_list
    else:
      result.append(element)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))
