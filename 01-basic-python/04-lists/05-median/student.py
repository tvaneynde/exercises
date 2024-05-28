def median(ns):
    sortedList = sorted(ns)
    index = len(ns) // 2
    if len(ns) % 2 == 0:
        return (sortedList[index - 1] + sortedList[index]) / 2

    else:
        return sortedList[index]
