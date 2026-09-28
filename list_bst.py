from base import BaseBST, BaseNode



class ListNode(BaseNode):


    def __init__(self, key):

        super().__init__(key)

        self.values = [key]




class ListBST(BaseBST):


    def insert(self, key):


        if self.root is None:

            self.root = ListNode(key)
            self._node_count += 1
            return



        current = self.root



        while True:


            if key == current.key:

                current.values.append(key)
                return



            elif key < current.key:


                if current.left is None:

                    current.left = ListNode(key)
                    self._node_count += 1
                    return


                current = current.left



            else:


                if current.right is None:

                    current.right = ListNode(key)
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


        total = 0



        def visit(node):

            nonlocal total


            if node:

                visit(node.left)


                total += len(node.values)


                visit(node.right)



        visit(self.root)


        return total