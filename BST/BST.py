from typing import List


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = Node(key, val)
        top = self.root
        if self.root is None:
            self.root = new_node
        else:
            while top is not None:
                if top.key < key:
                    if top.right is None:
                        top.right = new_node
                        break
                    else:
                        top = top.right
                elif top.key > key:
                    if top.left is None:
                        top.left = new_node
                        break
                    else:
                        top = top.left
                elif top.key == key:
                    top.value = val
                    break

    def get(self, key: int) -> int:
        top = self.root
        while top is not None:
            if top.key < key:
                top = top.right
            elif top.key > key:
                top = top.left
            elif top.key == key:
                return top.value
        return -1

    def getMin(self) -> int:
        top = self.root
        if self.root is None:
            return -1
        while top.left is not None:
            top = top.left

        return top.value

    def getMax(self) -> int:
        top = self.root
        if self.root is None:
            return -1
        while top.right is not None:
            top = top.right

        return top.value

    def displayNode(self, node, depth) -> None:
        if node is not None:
            self.displayNode(node.right, depth + 1)
            print("      " * depth, node.key)
            self.displayNode(node.left, depth + 1)

    def remove(self, key: int) -> None:
        top = self.root

        if top is None:
            return

        previous = None
        replacement = top.left
        replacement_parent = None

        if top.key == key:

            if self.root.left is not None and self.root.right is not None:
                while replacement is not None and replacement.right is not None:
                    replacement_parent = replacement
                    replacement = replacement.right

                self.root = replacement
                replacement.right = top.right

                if replacement is not None and replacement_parent is not None:
                    replacement_parent.right = replacement.left
                    self.root.left = top.left
                return

            elif self.root.left is not None and self.root.right is None:
                self.root = replacement
                return

            elif self.root.left is None and self.root.right is not None:
                self.root = top.right
                return
            else:
                self.root = None
                return

        while top is not None:
            if top.key > key:
                previous = top
                top = top.left
            elif top.key < key:
                previous = top
                top = top.right
            elif top.key == key:
                if top.left is None and top.right is None:
                    if previous.left == top:
                        previous.left = None
                        return
                    elif previous.right == top:
                        previous.right = None
                        return

                elif top.left is not None and top.right is None:
                    if previous.left == top:
                        previous.left = top.left
                        return
                    elif previous.right == top:
                        previous.right = top.left
                        return

                elif top.left is None and top.right is not None:
                    if previous.left == top:
                        previous.left = top.right
                        return
                    elif previous.right == top:
                        previous.right = top.right
                        return

                elif top.left is not None and top.right is not None:
                    replacement = top.left
                    while replacement.right is not None:
                        replacement_parent = replacement
                        replacement = replacement.right

                    if replacement_parent is None:
                        if previous.left == top:
                            previous.left = top.left
                            previous.left.right = top.right
                            return

                        elif previous.right == top:
                            previous.right = top.left
                            previous.right.right = top.right
                            return

                    elif replacement_parent is not None:
                        replacement_parent.right = replacement.left
                        if previous.left == top:
                            previous.left = replacement
                            replacement.left = top.left
                            replacement.right = top.right
                            return
                        elif previous.right == top:
                            previous.right = replacement
                            replacement.left = top.left
                            replacement.right = top.right
                            return

    def getInorderKeys(self) -> List[int]:
        keys = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            keys.append(node.key)
            inorder(node.right)

        inorder(self.root)
        return keys


if __name__ == "__main__":
    tm = TreeMap()
    tm.insert(4, 5)
    tm.insert(6, 5)
    tm.insert(3, 2)
    tm.insert(5, 5)
    tm.insert(8, 50)
    tm.insert(5, 23)
    tm.insert(12, 64)
    tm.displayNode(tm.root, 5)
