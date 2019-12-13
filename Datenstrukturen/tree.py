class TreeNode(object):
    """
    Binary Tree node
    """
    def __init__(self,key,lchild=None,rchild=None):
        self.key=key
        self.lchild=lchild
        self.rchild=rchild

def find(tree : TreeNode,key):
    if tree:
        if key < tree.key:
            return find(tree.lchild,key)
        if key > tree.key:
            return find(tree.rchild,key)
        return tree
    else:
        return None

def insert(tree, key):
    if not tree:
        return TreeNode(key)
    else:
        if key < tree.key:
            tree.lchild=insert(tree.lchild,key)
        elif key > tree.key:
            tree.rchild=insert(tree.rchild,key)
        else:
            print("Error duplicate Key: {}".format(key))
        return tree

def copyToArray(tree : TreeNode,arr):
    if tree:
        copyToArray(tree.lchild,arr)
        arr.append(tree.key)
        copyToArray(tree.rchild,arr)


def copyFromArray(tree,arr):
    if not tree:
        tree=TreeNode(0)

    for key in arr:
        insert(tree,key)
    return tree

def find_max(tree:TreeNode):
    while find_max(tree):
        while tree.rchild:
            tree=tree.rchild
    return tree

def delete(tree : TreeNode,key):
    if not tree:
        print("Error Key does not exist")
    if key < tree.key:
        tree.lchild=delete(tree.lchild,key)
    elif key > tree.key:
        tree.rchild=delete(tree.rchild,key)
    else:
        if tree.lchild and tree.rchild:
            max_node=find_max(tree.lchild)
            tmp=max_node.key
            max_node.key=tree.key
            tree.key=tmp
            tree.lchild=delete(tree.lchild,key)
        elif tree.lchild:
            return tree.lchild
        elif tree.rchild:
            return tree.rchild
    return tree

def rotate_r(tree:TreeNode):
    pivot=tree.lchild
    tree.lchild=pivot.rchild
    pivot.rchild=tree
    return pivot

def rotate_l(tree:TreeNode):
    pivot=tree.rchild
    tree.rchild=pivot.lchild
    pivot.lchild=tree
    return pivot

