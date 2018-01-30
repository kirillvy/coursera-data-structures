# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.result = str()

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])
            self.result =+ str(swap[0]), str(swap[1]), "\n"
        # print(self._data)

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        start = (len(self._data) // 2)
        # print(start)
        for i in reversed(range(0, start)):
            # print(i)
            self.siftdown(i)

    def siftdown(self, i):
        child = (i + 1) * 2 - 1
        child2 = (i + 1) * 2
        if child2 < len(self._data) and self._data[child2] < self._data[child]:
            child = child2
        if self._data[i] > self._data[child]:
            self._swaps.append((i, child))
            self._data[i], self._data[child] = self._data[child], self._data[i]
            if (child + 1) * 2 - 1 < len(self._data):
                self.siftdown(child)


    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
