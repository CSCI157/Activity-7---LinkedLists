class Node:
    def __init__(self, x, prev=None, nxt=None):
        self.prev = prev
        self.nxt = nxt
        self.data = x

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = node
            self.head.prev = None
            self.head.nxt = None
            self.tail = self.head
        else:
            self.tail.nxt = node
            node.prev = self.tail
            node.nxt = None
            self.tail = node

    def __str__(self):
        s = ""
        node = self.head
        while node is not None:
            s += str(node) + " "
            node = node.nxt
        return s
