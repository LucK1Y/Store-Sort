
"""
Test progam for AVL trees.
"""

import sys
import random
import getopt


class AVLNode(object):
    """
    Binary tree node.
    """

    def __init__(self, key, lchild=None, rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild
        self.balance = 0

    def recompute_balance(self):
        balance = height(self.lchild)-height(self.rchild)


class AVLTree(object):
    """
    Container type with the root of the tree.
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        #print "Inserting", key
        #print "-----------"
        #self.print_tree()
        #print "-----------"
        self.root, dummy = avl_insert(self.root, key)
        #print "-----------"
        #self.print_tree()
        #print "-----------"
        #print "Finished", key
        #print "==========="

    def insert_set(self, set, files=False):
        for k in set:
            self.insert(k)
            if files:
                dot_print_tree_full(self.root)

    def print_tree(self):
        print_tree(self.root)

    def find(self, key):
        return find(self.root, key)


def avl_insert(tree, key):
    """
    Insert a key into the tree. Return tupel of new tree and change in
    height (1 or 0).
    """
    if not tree:
        return AVLNode(key), 1
    elif key < tree.key:
        tree.lchild, delta = avl_insert(tree.lchild, key)
        if delta:
            tree.balance = tree.balance-delta
            if tree.balance == -2:
                print "Rebalance left", tree.key
                if tree.lchild.balance <= 0:
                    print "left-left"
                    tree, delta = avlrotate_r(tree)
                else:
                    print "left-right", tree.key
                    tree, delta = avlrotate_lr(tree)
                # We know from theoretical analyis that the tree depth
                # does not grow here
                return tree, 0
            else:
                # branch has possibly grown deeper
                return tree, abs(tree.balance)
        else:
            return tree, 0
    elif key > tree.key:
        tree.rchild, delta = avl_insert(tree.rchild, key)
        if delta:
            tree.balance = tree.balance+delta
            if tree.balance == 2:
                print "Rebalance right", tree.key
                if tree.rchild.balance >= 0:
                    print "right-right", tree.key
                    tree, delta = avlrotate_l(tree)
                else:
                    print "right-left", tree.key
                    tree, delta = avlrotate_rl(tree)
                return tree, 0
            else:
                # branch has possibly grown deeper
                return tree, abs(tree.balance)
        else:
                # We know from theoretical analyis that the tree depth
                # does not grow here
            return tree, 0
    else:
        print "Error: Duplicate key"
        return tree, 0


def avlrotate_rl(tree):
    tree.rchild, delta1 = avlrotate_r(tree.rchild)
    tree, delta2 = avlrotate_l(tree)
    return tree, delta2


def avlrotate_lr(tree):
    tree.lchild, delta1 = avlrotate_l(tree.lchild)
    tree, delta2 = avlrotate_r(tree)
    return tree, delta2


rtable = {
    (-1, 0): (0,  1,  0),
    (-1, -1): (1,  1,  0),
    (-1, 1): (0,  2,  0),
    (-2, -1): (0,  0, -1),
    (-2, -2): (1,  0, -1)}


def avlrotate_r(tree):
    pivot = tree.lchild
    tbal = tree.balance
    pbal = pivot.balance
    tree.lchild = pivot.rchild
    pivot.rchild = tree
    tree.balance, pivot.balance, delta = rtable[(tbal, pbal)]
    #print "L: (%2d,%2d) => (%2d, %2d, %2d)"%(tbal, pbal, tree.balance, pivot.balance, delta)
    return pivot, (-1+abs(pbal))


ltable = {
    (1, 0): (0, -1,  0),
    (1, 1): (-1, -1,  0),
    (1, -1): (0, -2,  0),
    (2, 1): (0,  0, -1),
    (2, 2): (-1,  0, -1)}


def avlrotate_l(tree):
    pivot = tree.rchild
    tbal = tree.balance
    pbal = pivot.balance
    tree.rchild = pivot.lchild
    pivot.lchild = tree
    tree.balance, pivot.balance, delta = ltable[(tbal, pbal)]
    #print "L: (%2d,%2d) => (%2d, %2d, %2d)"%(tbal, pbal, tree.balance, pivot.balance, delta)
    return pivot, delta


def tree_height(tree):
    if tree:
        return 1+max(tree_height(tree.lchild), tree_height(tree.rchild))
    else:
        return 0


def tree_bal(tree):
    if tree:
        return tree_height(tree.rchild) -\
            tree_height(tree.lchild)
    return 0


def find(tree, key):
    if tree:
        if key < tree.key:
            return find(tree.lchild, key)
        if key > tree.key:
            return find(tree.rchild, key)
        return tree


def print_tree(tree, indent=""):
    if tree:
        print_tree(tree.lchild, indent+"  ")
        bal = tree_height(tree.rchild)-tree_height(tree.lchild)
        marker = " "
        if bal != tree.balance:
            marker = "!"
        print "%s:%2d:%2d:%3d:%s %s" % (marker, tree.balance, bal,
                                        tree_height(tree), indent, tree.key)
        print_tree(tree.rchild, indent+"  ")


node_counter = 0


def newnode():
    global node_counter
    name = "H%02d" % (node_counter,)
    node_counter = node_counter+1
    return name


def dot_print_tree(tree, f=sys.stdout):
    if tree:
        #print >>f, "  %s [label=\"%s : %d\"]"%(tree.key,tree.key,tree.balance)
        print >>f, "  %s [label=\"%s\"]" % (tree.key, tree.key)
        if tree.lchild:
            print >>f, "  ", tree.key, "->", tree.lchild.key
        elif tree.rchild:
            hn = newnode()
            print >>f, "  ", hn, "[style=invis]"
            print >>f, "  ", tree.key, "->", hn, "[style=invis]"

        dot_print_tree(tree.lchild, f)
        if tree.rchild:
            print >>f, "  ", tree.key, "->", tree.rchild.key
        elif tree.lchild:
            hn = newnode()
            print >>f, "  ", hn, "[style=invis]"
            print >>f, "  ", tree.key, "->", hn, "[style=invis]"
        dot_print_tree(tree.rchild, f)


counter = 0


def newfile():
    global counter
    name = "avl%03d.gv" % (counter,)
    counter = counter+1
    print "Writing tp file", name
    return open(name, "w")


def dot_print_tree_full(tree):
    f = newfile()
    print >>f, """
digraph heap {
   rankdir=tb;
   ordering = out
"""
    print >>f,  "   HR [style=invisible]"
    if not tree:
        print >>f, "HN [style=invis]"
        print >>f, "   HR -> HN"
    else:
        print >>f, "   node [style=solid,fontname=Helvetica,fontsize=18]"
        print >>f, "   HR ->", tree.key
        dot_print_tree(tree, f)

    print >>f, """
}
"""
    f.close()


def print_keys(set):
    print "$K=\{",
    sep = ""
    for i in set:
        print sep, i,
        sep = ","
    print "\}$"


if __name__ == '__main__':
    opts, args = getopt.gnu_getopt(sys.argv[1:],
                                   "t",
                                   ["trees"])
    trees = False

    for opt, arg in opts:
        if opt == "-t" or opt == "--trees":
            trees = True

if not trees:
    keys = ["Max", "Moritz", "Fritz", "Franz", "Emil", "Herbert", "Anton",
            "Peter", "Paul", "Simon"]

    keys = range(30)
    #keys.reverse()
    random.seed(10)
    random.shuffle(keys)

    # Kl2016 ueb: keys = [16, 12, 20, 8, 14, 18, 22, 7, 10, 13, 24, 5]
    # keys = [26, 18, 34, 10, 22, 30, 36,  6, 14, 32, 40]
    keys = [16, 55, 19, 68, 72, 21, 33, 28, 15, 11, 40]
    tree = AVLTree()
    tree.insert_set(keys, True)

    tree.print_tree()
    print "================"
    dot_print_tree_full(tree.root)

    tree.insert(75)
    dot_print_tree_full(tree.root)

    tree.insert(17)
    dot_print_tree_full(tree.root)


else:
    pass
