def height(t):
    if is_leaf(t):
        return 0
    return 1 + max(height(branch) for branch in branch(t))


def max_path_sum(t):
    if is_leaf(t):
        return label(t)
    else:
        return max([max_path_sum(i) for i in branch(t)]) + label(t)

def square_tree(t):
    sq_branches = [square_tree(branch) for branch in branch(t)]
    return tree(label(t)**2, square_tree)

def find_path(tree, x):
    if label(tree) == x:
        return label(tree)
    for b in branch(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path