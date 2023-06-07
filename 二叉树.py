class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """a tree"""
        self.val = val
        self.left = left
        self.right = right
import PyQt5


class Treeclass:
    def __init__(self):
        self.root = None

    def built(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return

        def built(vals, node):
            if vals <= node.val:
                if node.left is None:
                    node.left = TreeNode(vals)
                else:
                    built(vals, node.left)

            if vals > node.val:
                if node.right is None:
                    node.right = TreeNode(vals)
                else:
                    built(vals, node.right)

        built(val, self.root)

    def preordertraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res += self.preordertraversal(root.left)
            res += self.preordertraversal(root.right)
        return res


Tree = Treeclass()
for i in range(10):
    Tree.built(i, )
print(Tree.preordertraversal(Tree.root))
