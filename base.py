from abc import ABC, abstractmethod


class BaseNode:

    def __init__(self, key):

        self.key = key
        self.left = None
        self.right = None



class BaseBST(ABC):

    def __init__(self):

        self.root = None
        self._node_count = 0



    @abstractmethod
    def insert(self, key):
        pass



    @abstractmethod
    def search(self, key):
        pass



    def is_empty(self):

        return self.root is None



    def node_count(self):

        return self._node_count



    def height(self):

        return self._height(self.root)



    def _height(self, node):

        if node is None:

            return -1


        return max(
            self._height(node.left),
            self._height(node.right)
        ) + 1



    def inorder(self):

        result = []

        self._inorder(self.root, result)

        return result



    def _inorder(self, node, result):

        if node:

            self._inorder(node.left, result)

            result.append(node.key)

            self._inorder(node.right, result)



    def preorder(self):

        result = []

        self._preorder(self.root, result)

        return result



    def _preorder(self, node, result):

        if node:

            result.append(node.key)

            self._preorder(node.left, result)

            self._preorder(node.right, result)



    def postorder(self):

        result = []

        self._postorder(self.root, result)

        return result



    def _postorder(self, node, result):

        if node:

            self._postorder(node.left, result)

            self._postorder(node.right, result)

            result.append(node.key)



    @abstractmethod
    def element_count(self):

        pass