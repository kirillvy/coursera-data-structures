#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):

    def numcheck(root):

        if tree[root][1] == -1:
            lgreatest, lleast = tree[root][0], tree[root][0]
        else:
            ltrue, lgreatest, lleast = numcheck(tree[root][1])
            if not ltrue or lgreatest > tree[root][0]:
                return False, 0, 0
        if tree[root][2] == -1:
            rgreatest, rleast = tree[root][0], tree[root][0]
        else:
            rtrue, rgreatest, rleast = numcheck(tree[root][2])
            if not rtrue or rleast < tree[root][0]:
                return False, 0, 0
        return True, rgreatest, lleast

    # Implement correct algorithm here
    mtrue, greatest, least = numcheck(0)
    if mtrue:
        return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    if nodes < 1:
        print("CORRECT")
        return
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
       print("CORRECT")
    else:
       print("INCORRECT")

threading.Thread(target=main).start()
