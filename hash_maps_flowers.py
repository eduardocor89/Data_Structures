"""
Blossom
The language of the flowers has a long history and has often been a topic resigned to the domain of dusty books in a thrift bookseller or a library.
With Blossom, we want to give people lightning fast access to all of the possible meanings of their favorite flowers.
In this project, we are going to implement a hash map to relate the names of flowers to their meanings. 
In order to avoid collisions when our hashing function collides the names of two flowers, we are going to use separate chaining. 
We will implement the Linked List data structure for each of these separate chains.

"""
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for item in range(self.array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])

    list_at_array = self.array[array_index]

    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return

    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]

    for item in list_at_index:
      if key == item[0]:
        return item[1]
      else:
        return None

# Now let's create a new instance of a HashMap called blossom and assign
# every element of flower_definitions to keys and values

blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
  print(element[0],element[1])
  blossom.assign(element[0],element[1])
print()
print(blossom.retrieve('daisy'))
print(blossom.retrieve('snapdragon'))

# and it works as expected!
