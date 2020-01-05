class Node(object):
    def __init__(self):
        self.data = data
        self.next = None

class Queue(object):

    def __init__(self):
        self.front = self.rear = None

    def isempty(self): 
        return self.front == None

    def enqueue(self, data):
        if self.rear is None:
            self.front = self.rear = Node(data)
            self.front = Node(data)
        else:
            new_Node = Node(data)
            new_Node.rear.next = new_Node
            self.rear = new_Node

    def dequeue(self):
        if self.isempty():
            print('queue is empty')
        else:
            node = self.front
            self.front = node.next
            if (self.front == None):
                self.rear = None
            return node.data

    def traverse(self):
        if self.isempty():
            print('queue is empty')
        else:
            while(self.rear != None):
                print('value ', self.front.data)
                self.rear = self.rear.next

q = Queue();
q.traverse()
q.enqueue(1)
q.enqueue(10)
q.traverse()
d.dequeue()
q.traverse()
q.enqueue(100)
q.enqueue(1000)
q.traverse()
q.dequeue()
q.traverse()
