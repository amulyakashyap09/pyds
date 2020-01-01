# implementation of stack using linkedlist

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  
  def __init__(self):
    self.head = None

  def isempty(self): 
      if self.head == None: 
          return True
      else: 
          return False
  
  def push(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      new_Node = Node(data)
      new_Node.next = self.head
      self.head = new_Node
  
  def pop(self):
    if self.head is None:
      print('cannot pop as stack is empty ')
      return None
    else:
      popped = self.head.data
      self.head = self.head.next
      return popped
  
  def traverse(self):
    node = self.head
    if (self.isempty()):
      print('empty stack')
    else:
      while(node != None):
        print('value ', node.data)
        node = node.next

stack = Stack()
stack.push(1)
stack.push(10)
stack.push(100)
stack.traverse()
