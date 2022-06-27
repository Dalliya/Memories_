from bisect import bisect_left

def contains(l, elem):
    index = bisect_left(l, elem)
    if index < len(l):
        return l[index] == elem
    return False

print(contains(list(range(1000)), -10))


