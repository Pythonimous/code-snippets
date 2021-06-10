class BinaryNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

    def insert(self, value):
        if self.value:
            if self.next is None:
                self.next = ListNode(value)
            else:
                self.next.insert(value)
        else:
            self.value = value

    def traverse(self):
        pointer = self
        while pointer:
            print(pointer.value)
            pointer = pointer.next

example = ListNode(1)

example.insert(2)
example.insert(3)

example.traverse()
