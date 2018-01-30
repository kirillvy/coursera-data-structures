# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = [max(lines)]


def getParent(table):
    # find parent and compress path
    if table == parent[table]:
        return parent[table]
    else:
        return getParent(parent[table])


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    if rank[realSource] > rank[realDestination]:
        realDestination, realSource = realSource, realDestination

        # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    parent[realSource] = realDestination
    lines[realDestination] += lines[realSource]
    rank[realDestination] += rank[realSource]

    if rank[realDestination] == rank[realSource]:
        rank[realDestination] += 1

    if lines[realDestination] > ans[0]:
        ans[0] = lines[realDestination]
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans[0])
