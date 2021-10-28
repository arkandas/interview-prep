# LIFO Structure: Last item we insert is the first item we take out

class Stack:

    def __init__(self):
        # One dimensional array
        self.stack = []

    # PUSH -> Implement the push method -> O(1)
    def push(self, data):
        self.stack.append(data)

    # POP -> Implement the pop method to get the first element of the stack -> O(1)
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # PEEK -> Returns the last inserted item without removing it -> O(1)
    def peek(self):
        return self.stack[-1]

    # Check stack size -> O(1)
    def is_empty(self):
        return self.stack == []

    # Return number of elements on the stack
    def stack_size(self):
        return len(self.stack)

