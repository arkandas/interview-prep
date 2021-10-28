class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        # If there is no node at the head position, the linkedList is empty so we
        # have to initialize the head node
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def size_of_linkedList(self):
        return self.numOfNodes

    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def remove(self, data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node.data != data and actual_node is not None:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        # Search miss, the item is not present in the linked list
        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode


    def get_middle_node(self):

        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer

    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node



