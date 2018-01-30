# python3

# import unittest

class JobQueue:
    def read_data(self):
            self.num_workers, m = map(int, input().split())
            self.jobs = list(map(int, input().split()))
            assert m == len(self.jobs)
            # self.result = str()

    def write_response(self):
        for i in range(len(self.jobs)):
            # self.result += (str(self.assigned_workers[i]) + " " + str(self.start_times[i]) + "\n")
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self._data = [[_, 0] for _ in range(self.num_workers)]
        for i in range(len(self.jobs)):
            self.assigned_workers[i] = self._data[0][0]
            self.start_times[i] = self._data[0][1]
            self._data[0][1] += self.jobs[i]
            self.siftdown(0)

    def siftdown(self, i):
        select = i
        left = (i + 1) * 2 - 1
        right = (i + 1) * 2

        if left < self.num_workers:
            if self._data[left][1] < self._data[select][1]:
                select = left
            elif self._data[left][1] == self._data[select][1] and self._data[left][0] < self._data[select][0]:
                select = left
        if right < self.num_workers:
            if self._data[right][1] < self._data[select][1]:
                select = right
            elif self._data[right][1] == self._data[select][1] and self._data[right][0] < self._data[select][0]:
                select = right
        if i != select:
            self._data[i], self._data[select] = self._data[select], self._data[i]
            self.siftdown(select)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

# class MyTest(unittest.TestCase):
#
#     def testOne(self):
#         job_queue.solve()
#         a = open('tests/08.a', 'r')
#         self.assertEqual(a.read(), job_queue.result)
#         print("successful.")
#         a.close()

if __name__ == '__main__':
    job_queue = JobQueue()
    # unittest.main()
    job_queue.solve()

