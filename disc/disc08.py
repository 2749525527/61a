from os import pathsep


>>> A("one")

nothing

>>> print(A("one"))

def sum_nums(lnk):
    if lnk == Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)

def multiply_lnk(lnk_of_lnks):
    product = 1
    for ink in lnk_of_lnk:
        if ink is List_empty:
            return Link.empty
        product *= lnk.fist
    lst_of_lnk = [ink.rest for ink in lst_of_lnk]
    return Link(product, multiply_lnk(lst_of_lnk))

def flip_two(lnk):
     if lnk is Link.empty or lnk.rest is Link.empty:
         return
    lnk.fist, lnk.rest.first = lnk.rest.first, lnk.fist
    return flip_two(lnk.rest.rest)

def filter_link(link, f):
    while link is Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest
def make_even(t):
    if t.label % 2 != 0:
        t.label += 1
    for branch in t.bracnches:
        make_even(branch)
def square_tree(t):
    t.label = t.tabel ** 2
    for branch in t.branches:
        square_tree(branch)
def find_paths(t, entry):
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for branch in t.branches:
        for branch in find_paths(branch, entry):
            paths.append([t.label] + path)
    return paths
def find_paths(t, entry):
    paths = []
    if t.label == entry:
         paths.append([t.label])
    for b in t.branches: 
        branch_paths = [[t.label] + path for path in find_paths(b, entry)] 
        paths.extend(branch_paths) 
    return paths
def combine_tree(t1, t2, combiner):
    combined = [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), combined)
def alt_tree_map(t, map_fn):
    def helper(t, depth):
        if depth % 2 == 0:
            label = map_fn(t.label)
        else：
            label = t.label
        branches = [helper(b, depth + 1) for b in t.branches]
        return Tree(label, branches)
    return helper(t, 0)