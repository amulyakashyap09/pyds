class Node:
  def __init__(self, data):
    self.data = data
    self.ref = None

class LinkedList:

  def __init__(self):
    self.start_node = None

  def traverse_list(self):
    if self.start_node is None:
      print("List is empty")
    else:
      node = self.start_node
      while(node is not None):
        print(node.data , " ")
        node = node.ref

  def insert_at_start(self, data):
    # create a new node first
    new_node = Node(data)
    new_node.ref = self.start_node
    self.start_node = new_node

  def insert_at_end(self, data):
    # create a new node first
    new_node = Node(data)
    # traverse the list
    if self.start_node is None:
      self.start_node = new_node
      return
    
    node = self.start_node
    while(node.ref is not None):
      node = node.ref
    node.ref = new_node

  def insert_after_item(self, value, data):
    if self.start_node is None:
      print("empty list cannot insert before given value")
      return
    else:
      node = self.start_node
      valueFound = False
      new_node = Node(data)
      while (node is not None):
        if node.data == value:
            node = node.ref
            valueFound = True
            new_node.ref = node
            node = new_node
            break
      if valueFound == False:
        print ("value not present in the linked list")
        return

  def insert_before_item(self, value, data):

    if self.start_node is None:
      print("empty list cannot insert before given value")
      return
    
    if self.start_node.data == value:
      new_node = Node(data)
      new_node.ref = self.start_node
      self.start_node = new_node
      return

    node = self.start_node
    valueFound = False
    new_node = Node(data)
    while (node.ref is not None):
      if node.data == value:
          node = node.ref
          valueFound = True
          new_node.ref = node.ref
          node.ref = new_node
          break
    if valueFound == False:
      print ("value not present in the linked list")
      return

  def insert_at_index(self, index, data):
    
    if index == 0:
      new_node = Node(data)
      new_node.ref = self.start_node
      self.start_node = new_node
      return
    
    i=0
    node = self.start_node
    while(i<index and node is not None):
      node = node.ref
      i=i+1
    
    if node is None:
      print('Index out of bound')
      return
    else:
      new_node = Node(data)
      new_node.ref = node.ref
      node.ref = new_node




new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_start(20)
new_linked_list.insert_at_start(40)
new_linked_list.insert_at_index(3, 30)
new_linked_list.traverse_list()
