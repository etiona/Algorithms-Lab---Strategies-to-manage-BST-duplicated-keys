from base import BaseBST, BaseNode


class FlagNode(BaseNode):

    def __init__(self, key):
        super().__init__(key)

        # False = prossimo duplicato a sinistra
        # True = prossimo duplicato a destra
        self.flag = False


class FlagBST(BaseBST):

    def insert(self, key):

        if self.root is None:
            self.root = FlagNode(key)
            self._node_count += 1
            return

        current = self.root

        while True:

            if key == current.key:

                if current.flag:

                    # flag True -> destra
                    if current.right is None:
                        current.right = FlagNode(key)
                        self._node_count += 1
                        current.flag = False
                        return

                    current.flag = False
                    current = current.right

                else:

                    # flag False -> sinistra
                    if current.left is None:
                        current.left = FlagNode(key)
                        self._node_count += 1
                        current.flag = True
                        return

                    current.flag = True
                    current = current.left

            elif key < current.key:

                if current.left is None:
                    current.left = FlagNode(key)
                    self._node_count += 1
                    return

                current = current.left

            else:

                if current.right is None:
                    current.right = FlagNode(key)
                    self._node_count += 1
                    return

                current = current.right

    def search(self, key):

        current = self.root

        while current:

            if key == current.key:
                return True

            elif key < current.key:
                current = current.left

            else:
                current = current.right

        return False

    def delete(self, key):

        pass

    def element_count(self):
        return self._node_count

    def print_tree(self):

        def _print(node, level, position):

            if node is None:
                return

            print(
                "    " * level
                + f"{position}: key={node.key}, flag={node.flag}"
            )

            _print(node.left, level + 1, "L")
            _print(node.right, level + 1, "R")

        if self.root is None:
            print("Albero vuoto")
        else:
            _print(self.root, 0, "Root")


# TEST
if __name__ == "__main__":

    tree = FlagBST()

    data = [5, 5, 5, 5, 5]

    for value in data:
        tree.insert(value)

    print("Albero:")
    tree.print_tree()