class Node:
    def __init__(self, node):
        self.node = node
        self.fchild = None
        self.siblings = None

class MgTree:
    def __init__(self, r_node):
        self.r_node = r_node

    def add_fchild(self, x, y):
        x.fchild = y

    def add_siblings(self, x, y):
        x.siblings = y


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
i = Node('I')
j = Node('J')
k = Node('K')
l = Node('L')
m = Node('M')
n = Node('N')
o = Node('O')
p = Node('P')
q = Node('Q')
r = Node('R')
s = Node('S')

tree = MgTree(a)
tree.add_fchild(a, b)
tree.add_siblings(b, c)
tree.add_siblings(c, d)
tree.add_siblings(d, e)
tree.add_fchild(e, h)
tree.add_fchild(b, f)
tree.add_fchild(d, g)
tree.add_fchild(f, i)
tree.add_siblings(i, j)
tree.add_siblings(j, k)
tree.add_fchild(g, l)
tree.add_siblings(l, m)
tree.add_fchild(i, n)
tree.add_fchild(k, o)
tree.add_fchild(m, p)
tree.add_siblings(p, q)
tree.add_siblings(q, r)
tree.add_fchild(q, s)


def tree_traversal(tree):
    S = []
    V = set()
    root_node = tree.r_node
    S.append(root_node)
    while root_node.fchild:
        S.append(root_node.fchild)
        root_node = root_node.fchild
    while S:
        n = S.pop()
        print(n.node)
        V.add(n)
        if S:
            while S[-1].fchild in V or S[-1].siblings not in V:
                if S[-1].fchild and S[-1].fchild not in V:
                    S.append(S[-1].fchild)
                elif S[-1].siblings and S[-1].siblings not in V:
                        S.append(S[-1].siblings)
                else:
                    break
            x = [i.node for i in S]
    return "Completed"


print(tree_traversal(tree))







