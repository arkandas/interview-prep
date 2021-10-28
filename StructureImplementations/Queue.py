# QUEUE -> FIFO Structure -> In can be implemented with dynamic arrays as well with linked lists
# Can be implemented with a stack or with a linked list

class Queue:

    def __init__(self):
        self.queue = []

    # O(1) running time complexity
    def is_empty(self):
        return self.queue == []

    # O(1) running time complexity
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            print("The queue is already empty")
            return -1

    # O(1) running time
    def peek(self):
        return self.queue[0]

    # O(1) running time
    def size_queue(self):
        return len(self.queue)