# python3

import sys, threading
#import unittest
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = list()
        self.nodes = []
        self.root = int()

    def read(self, *args):
        if args:
            self.n = int(args[0])
            self.parent = list(map(int, args[1].split()))
        else:
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
        self.nodes = [[] for _ in range(self.n)]

    def build_tree(self):
        for i, parent_index in enumerate(self.parent):
            if parent_index == -1:
                self.root = i
            else:
                self.nodes[parent_index].append(i)
        # print(self.nodes)

    def compute_height(self, *args):
        # Replace this code with a faster implementation
        if args:
            index = args[0]
        else:
            index = self.root
        if not self.nodes[index]:
            return 1
        return 1 + max(self.compute_height(_) for _ in self.nodes[index])


# class MyTest(unittest.TestCase):
#     def testOne(self):
#         tree = TreeHeight()
#         for x in range(1, 25):
#             if x < 10:
#                 x = str(x)
#                 x = '0'+x
#             else:
#                 x = str(x)
#             print("Test", x, "... ", end="")
#             t = open('tests/'+x, 'r')
#             a = open('tests/'+x+'.a', 'r')
#             tree.read(t.readline(), t.readline())
#             tree.build_tree()
#             self.assertEqual(str(tree.compute_height()), a.readline().rstrip())
#             print("successful.")
#             t.close()
#             a.close()


def main():
    # unittest.main(verbosity=2)
    tree = TreeHeight()
    tree.read()
    tree.build_tree()
    print(tree.compute_height())


threading.Thread(target=main).start()
