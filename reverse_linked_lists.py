
# to create a new node
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None


	def traverse(self):
		node = self.head
		if (node == None):
			print('list is empty')
			return
		else:
			while(node != None):
				print('value : ', node.data)
				node = node.next

	
	def push(self, data):

		if self.head is None:
		  self.head = Node(data)
		else:
		  new_Node = Node(data)
		  new_Node.next = self.head
		  self.head = new_Node

	def reverse(self):

		prevNode = None
		currNode = self.head
		nextNode = None

		while(currNode != None):
			nextNode = currNode.next
			currNode.next = prevNode
			prevNode = currNode
			currNode = nextNode

		self.head = prevNode


	def reverseUsingRecursion(self, currNode, prevNode):

		if (currNode.next == None):
			self.head = currNode
			currNode.next = prevNode
			return
		else:
			nextNode = currNode.next
			currNode.next = prevNode
			self.reverseUsingRecursion(nextNode, currNode)

	def recursiveReverse(self):

		if self.head is None:
			print('list is empty')
		else:
			self.reverseUsingRecursion(self.head, None)


ll = LinkedList()
ll.traverse()
ll.push(1)
ll.push(10)
ll.push(100)
ll.traverse()
ll.reverse()
ll.traverse()
ll.recursiveReverse()
ll.traverse()
