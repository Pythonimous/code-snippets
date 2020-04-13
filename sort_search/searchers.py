from sorters import Sorters


class Searchers:
    def __init__(self, reference, search_key):
        self.reference = reference
        self.key = search_key

    def non_recursive_binary_search(self):  # CS.11
        to_search = self.reference
        prefix = 0
        while len(to_search) >= 1:
            mid = len(to_search) // 2
            if to_search[mid] == self.key:
                return prefix + mid
            elif to_search[mid] > self.key:
                to_search = to_search[:mid]
            else:
                prefix += mid+1
                to_search = to_search[mid+1:]
        return -1

    def binary_search(self, lo=0, hi=0):
        if hi == 0:
            hi = len(self.reference)

        if hi <= lo:
            return -1
        mid = lo + (hi-lo)//2

        if self.reference[mid] > key:
            return self.binary_search(lo, mid)
        elif self.reference[mid] < key:
            return self.binary_search(mid+1, hi)
        else:
            return mid

    def test_algorithm(self, algorithm):
        """
        Tests one of the searching algorithms of a class.
        :param algorithm: one of the following: "binary", "non_recursive_binary"
        :return:
        """
        unsorted = ' '.join(self.reference)
        print(f'Searching for {self.key} in {unsorted}.')
        print(f'Testing {algorithm}.')
        if algorithm == 'non_recursive_binary':
            found_position = self.non_recursive_binary_search()
        elif algorithm == 'binary':
            found_position = self.binary_search()
        else:
            found_position = -2
        if found_position >= 0:
            print(f'{self.key} found at position {found_position}')
            print(f'Element at position {found_position}: {self.reference[found_position]}\n')
        elif found_position == -1:
            print('No such key found.\n')
        elif found_position == -2:
            print("An algorithm doesn't exist.\n")


if __name__ == "__main__":
    # Testing block
    unsorted_list = ['dog', 'apple', 'kate', 'awoo', 'werewolf', 'god']
    testing_list = Sorters(unsorted_list).merge_sort()

    key = 'god'
    searcher = Searchers(testing_list, key)

    searcher.test_algorithm('non_recursive_binary')
    searcher.test_algorithm('binary')
