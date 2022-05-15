def total_ones(n):
    i, total = 1, 0
    while i <= n:
        total += count_one(i)
        i += 1
    return total