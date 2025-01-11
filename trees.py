def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]#存储树的值

def branches(tree):#存储树的叶子
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:#树为空
        return False
    for branch in branches(tree):#有子树不是树
        if not is_tree(branch):
            return False
    return True

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)
