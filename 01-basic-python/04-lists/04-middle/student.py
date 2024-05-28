def middle(ns):
    length = len(ns)
    mid = length // 2
    for n in range(0, length):
        if n == mid:
            return ns[n]
