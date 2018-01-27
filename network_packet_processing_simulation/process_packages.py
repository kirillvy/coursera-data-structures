# python3

import unittest
<<<<<<< HEAD
from collections import deque
=======
>>>>>>> 90ce406751a4d87b2ce23e10ce6f6a66b7e470ee

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = deque()

    def Process(self, request):
        # # write your code here
        while self.finish_time_:
            if request.arrival_time >= self.finish_time_[0]:
                self.finish_time_.popleft()
            else:
                break

        if len(self.finish_time_) >= self.size:
            return Response(True, -1)

        else:
            if len(self.finish_time_) == 0:
                self.finish_time_.append(request.arrival_time + request.process_time)
                return Response(False, request.arrival_time)
            else:
                rtime = self.finish_time_[len(self.finish_time_) - 1]
                if request.arrival_time >= rtime:
                    self.finish_time_.append(request.arrival_time + request.process_time)
                    return Response(False, request.arrival_time)
                else:
                    self.finish_time_.append(rtime + request.process_time)
                    return Response(False, rtime)


def ReadRequests(count, *args):
    requests = []
    if args:
        tfile = args[0]
        for i in range(count):
            arrival_time, process_time = map(int, tfile.readline().strip().split())
            requests.append(Request(arrival_time, process_time))
    else:
        for i in range(count):
            arrival_time, process_time = map(int, input().strip().split())
            requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        response = buffer.Process(request)
        if response:
            responses.append(response)
    # while buffer.finish_time_:
    #     responses.append(buffer.emptyQueue())
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

class MyTest(unittest.TestCase):
    def testOne(self):
        for x in range(1, 23):
            if x < 10:
                x = str(x)
                x = '0'+x
            else:
                x = str(x)
            print("Test", x, "... ", end="")
            t = open('tests/'+x, 'r')
            a = open('tests/'+x+'.a', 'r')
            tsize, tcount = map(int, t.readline().strip().split())
            trequests = ReadRequests(tcount, t)
            testoutput = str()
            tbuffer = Buffer(tsize)
            tresponses = ProcessRequests(trequests, tbuffer)
            for i, response in enumerate(tresponses):
                testoutput += str(response.start_time if not response.dropped else -1)
                if i >= 0:
                    testoutput += "\n"
            self.assertEqual(testoutput, a.read())
            print("successful.")
            t.close()
            a.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
