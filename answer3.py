def recur(n, cur):
    if not cur:
        cur = 0
    if n < 1:
        raise ("Invalid input")
    else:
        for i in range(2, n + 1):
            cur += 1 / (i * (i - 1))
        return cur
