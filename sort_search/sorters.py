class Sorters:
    def __init__(self, to_sort):
        self.to_sort = to_sort

    def bubble_sort(self, to_sort=''):
        if not to_sort:
            to_sort = self.to_sort

        counter = 0
        full_pass = False
        while not full_pass:
            for i in range(len(to_sort) - 1):
                if to_sort[i] > to_sort[i+1]:
                    to_sort[i], to_sort[i+1] = to_sort[i+1], to_sort[i]
                    counter += 1
            if counter == 0:
                full_pass = True
            else:
                counter = 0
        return to_sort

    def insertion_sort(self, to_sort=''):
        if not to_sort:
            to_sort = self.to_sort

        for i in range(1, len(to_sort)):
            for j in range(i, 0, -1):
                if to_sort[j-1] > to_sort[j]:
                    to_sort[j], to_sort[j-1] = to_sort[j-1], to_sort[j]
                else:
                    break
        return to_sort

    #  Merge sort
    @staticmethod
    def merge(to_merge, lo, mid, hi):
        aux = []
        i = lo
        j = mid
        n = hi - lo
        for _ in range(n):
            if i == mid:
                aux.append(to_merge[j])
                j += 1
            elif j == hi:
                aux.append(to_merge[i])
                i += 1
            elif to_merge[i] <= to_merge[j]:
                aux.append(to_merge[i])
                i += 1
            else:
                aux.append(to_merge[j])
                j += 1
        for k in range(len(aux)):
            to_merge[k + lo] = aux[k]
        return to_merge

    def merge_sort(self, to_sort='', lo=0, hi=0):
        if hi == 0:
            hi = len(to_sort)
        n = hi - lo
        if n <= 1:
            return to_sort
        mid = lo + n//2
        to_sort = self.merge_sort(to_sort, lo, mid)
        to_sort = self.merge_sort(to_sort, mid, hi)
        to_sort = self.merge(to_sort, lo, mid, hi)
        return to_sort

    def test_algorithm(self, algorithm):
        """
        Tests one of the sorting algorithms of a class.
        :param algorithm: one of the following: "bubble", "insertion", "merge"
        :return:
        """
        unsorted = ' '.join(self.to_sort)
        print(f'Testing {algorithm}. To sort: {unsorted}')
        if algorithm == 'bubble':
            sorted_list = ' '.join(self.bubble_sort(self.to_sort))
        elif algorithm == 'insertion':
            sorted_list = ' '.join(self.insertion_sort(self.to_sort))
        elif algorithm == 'merge':
            sorted_list = ' '.join(self.merge_sort(self.to_sort))
        else:
            sorted_list = None

        if sorted_list:
            print(f'Sorted: {sorted_list}\n')
        else:
            print(f'{algorithm}: No such method.\n')


if __name__ == "__main__":
    # Testing block
    testing_list = ['dog', 'apple', 'kate', 'awoo', 'werewolf', 'god']

    sorter = Sorters(testing_list)
    sorter.test_algorithm('bubble')
    sorter.test_algorithm('insertion')
    sorter.test_algorithm('merge')
