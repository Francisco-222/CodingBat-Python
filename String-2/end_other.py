def end_other(a, b):
    base   = a.lower()
    search = b.lower()
    if len(a) < len(b):
        base   = b.lower()
        search = a.lower()

    return base.endswith(search)
