from tree import BinaryTree

def tree_intersection(treeOne, treeTwo):
    if not treeOne or not treeTwo:
        return None

    values = dict()

    def walk(root):
        if not root:
            return
        values[root.value] = values.get(root.value, 0) + 1
        walk(root.left)
        walk(root.right)
        return values

    walk(treeOne.root)
    walk(treeTwo.root)

    return list({key for (key, value) in values.items() if value > 1})






