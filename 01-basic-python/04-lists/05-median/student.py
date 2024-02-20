def median(ns):
    sort = sorted(ns)
    if len(ns) % 2 == 0:
        return (sort[len(ns) // 2 - 1] + sort[len(ns) // 2]) / 2
    else:
        return sort[len(ns) // 2]
