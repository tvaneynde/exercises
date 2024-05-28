def contains_duplicates(xs):
    noDupes = sorted(list(set(xs)))
    return not noDupes == sorted(xs)
