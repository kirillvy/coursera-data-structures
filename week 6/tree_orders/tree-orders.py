# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def inOrderFunc(root, result):
            if self.left[root] != -1:
                inOrderFunc(self.left[root], result)
            result.append(self.key[root])
            if self.right[root] != -1:
                inOrderFunc(self.right[root], result)

        inOrderFunc(0, result)

        return result

    def preOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def preOrderFunc(root, result):
            result.append(self.key[root])
            if self.left[root] != -1:
                preOrderFunc(self.left[root], result)
            if self.right[root] != -1:
                preOrderFunc(self.right[root], result)

        preOrderFunc(0, result)
        return result

    def postOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def postOrderFunc(root, result):
            if self.left[root] != -1:
                postOrderFunc(self.left[root], result)
            if self.right[root] != -1:
                postOrderFunc(self.right[root], result)
            result.append(self.key[root])

        postOrderFunc(0, result)
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
