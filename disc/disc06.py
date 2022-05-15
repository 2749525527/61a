def memory(n):
    def f(g):
        nonlocal n
        return g(n)
    return f

// i don't understand mystery function what's mean

def group_by(s, fn):
    grouped = {}
    for x in s:
        key = fn(x)
        if key in grouped:
            grouped[key].append(x)
        else:
            grouped[key]=[x]
    return grouped

def add_this_many(x, el, s):
    i = 0
    while(i < x):
        s.append(el)
        i += 1
def filter(iterable, fn):
    for x in iterable:
        if fn(x):
            yield x

def merge(a , b):
    next_a, next_b = next(a), next(b)
    if next_a == next_b:
        yield next_a
        next_a, next_b = next(a), next(b)
    elif next_a < next_b:
        yield next_a
        next_a = next(a)
    else:
        yield next_b
        next_b = next(b)