class TreeComparator(object):
    def compareTrees(self, node1, node2):

        # Check the base cases
        if not node1 or not node2:
            return node1==node2
        # Check the values within the nodes
        if node1.data is not node2.data:
            return false
        # Go for the subtrees, the have to match as well
        return self.compareTrees(node1.left_child, node2_left_child) and self.compareTrees(node1.right_child, node2.right_child)

class Node:

    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent



class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    # O(logN)
    def insert_node(self, node):

        # Check Left SubTree
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)

        # Check Right SubTree
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)


    def traverse(self):
        if self.root is not Node:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print('%s' % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):

        actual = self.root

        while actual.rightChild is not None:
            actual = actual.rightChild

        return actual.data

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        if data > node.data:
            self.remove_node(data, node.rightChild)

        else:
            if node.leftChild is None and node.rightChild is None:
                print('removing node: %d' % node.data)
                parent = node.parent
                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:
                print('removing a node with a single right child')

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.leftChild is not None and node.rightChild is None:
                print('removing a node with a single left child')

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print('removing node with two children...')

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node




