def contains_duplicates(xs):
    noDupes = sorted(list(set(xs)))
    return noDupes != sorted(xs)
