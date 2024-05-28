def drop_nth(xs, n):
    l = []
    for i in range(len(xs)):
        if i == n:
            continue
        else:
            l.append(xs[i])
    return l


drop_nth([1, 2, 3], 0)
