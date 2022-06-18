# Lists

for i in range(1, 1000):
    v = i
    v2 = i
    if id(v) != id(v2):
        print('found: %d' % v)
        break
