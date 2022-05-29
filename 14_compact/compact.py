def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    falsyRemoved = []

    for item in lst:
        if (bool(item)):
            falsyRemoved.append(item)
    return falsyRemoved