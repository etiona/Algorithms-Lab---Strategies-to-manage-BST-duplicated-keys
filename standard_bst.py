from base import BaseBST, BaseNode


class StandardNode(BaseNode):
    pass



class StandardBST(BaseBST):


    def insert(self, key):

        new_node = StandardNode(key)


        if self.root is None:

            self.root = new_node
            self._node_count += 1
            return



        current = self.root


        while True:

            if key < current.key:


                if current.left is None:

                    current.left = new_node
                    break


                current = current.left


            else:
                # duplicati inseriti nel sottoalbero destro

                if current.right is None:

                    current.right = new_node
                    break


                current = current.right



        self._node_count += 1



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