class Node(object):
    def __init__(self, item, next_item):
        self.item = item
        self.next = next_item


class Stack:
    def __init__(self):
        self.first = None
        self.length = 0

    def is_empty(self):
        """
        Checks if the stack is empty
        :return: True or False respectively
        """
        return self.first is None

    def push(self, item):
        """
        Pushes element to the stack
        :param item: value to be pushed
        """
        second = self.first
        self.first = Node(item, second)
        self.length += 1

    def pop(self):
        """
        Removes element from the stack and returns its value
        :return: value of the element (LIFO)
        """
        item = self.first.item
        self.first = self.first.next
        self.length -= 1
        return item

    def size(self):
        """
        Returns size of the stack
        """
        return self.length

    def test(self, input_file):
        """
        Tests all functions
        :param input_file: text file with '-' among words
        :return:
        """
        with open(input_file, 'r') as f:
            to_test = f.read().strip().split()
        f.close()
        for t in to_test:
            if t == '-':
                print(self.pop())
            else:
                self.push(t)

        print(self.size())
        while self.first:
            print(self.pop())
        print(self.is_empty())


if __name__ == '__main__':
    stack = Stack()
    stack.test('test.txt')
