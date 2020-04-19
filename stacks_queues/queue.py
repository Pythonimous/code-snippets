class Node(object):
    def __init__(self, item, next_item):
        self.item = item
        self.next = next_item


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def is_empty(self):
        """
        Checks if the queue is empty
        :return: True or False respectively
        """
        return self.first is None

    def enqueue(self, item):
        """
        Adds element to the queue
        :param item: value to add
        """
        old_last = self.last
        self.last = Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.length += 1

    def dequeue(self):
        """
        Removes element from the queue and returns its value
        :return: value of the first element of the queue (FIFO)
        """
        item = self.first.item
        self.first = self.first.next
        self.length -= 1
        if self.is_empty():
            self.last = None
        return item

    def remove_after(self, value):
        """
        Removes element after the one with the given value
        :param value: element preceding the one for removal
        """
        t = self.first
        while t is not None:
            if t.item == value:
                t.next = t.next.next
                self.length -= 1
                break
            else:
                t = t.next

    def size(self):
        """
        Returns length of the queue
        :return: length of the queue
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
                print(self.dequeue())
            else:
                self.enqueue(t)

        print(self.size())
        self.remove_after('the')

        print(self.size())
        while self.first:
            print(self.dequeue())
        print(self.is_empty())


if __name__ == '__main__':
    queue = Queue()
    queue.test('test.txt')
