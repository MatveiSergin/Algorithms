class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if node.data == value:
            return node, parent, True
        if node.data > value:
            if node.left:
                return self.__find(node.left, node, value)
        if node.data < value:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return

        visited = [node]

        while visited:
            cur_v = []
            for x in visited:
                print(x.data, end=" ")
                if x.left:
                    cur_v += [x.left]
                if x.right:
                    cur_v += [x.right]
            print()
            visited = cur_v.copy()
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        if p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            else:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            else:
                p.right = s.left
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent
    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr, = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)
v = [10, 5, 7, 16, 13, 2, 20]

tree = Tree()

for x in v:
    tree.append(Node(x))
tree.show_wide_tree(tree.root)
print()
tree.del_node(5)
tree.show_wide_tree(tree.root)