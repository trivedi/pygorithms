'''
Finds min value of stack in O(1) time using O(n) space

In the worst case, it takes O(n) (w/ a constant factor of 2) space, but on
average it does slightly better because we don't keep a duplicate copy of
every item in the stack.
'''


class Stack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, item):
        """Add item to top of stack"""
        self._stack.append(item)

        # Maintain shadow stack that only contains min items
        if (not self._min_stack):
            # First element of both stacks
            self._min_stack.append(item)
        else:
            # Only add item to shadow stack if it's less
            # than the 'local minimum', viz. a minimum
            # element that is below the current stack position
            if item <= self._min_stack[-1]:
                self._min_stack.append(item)

    def pop(self):
        """Remove and return item at the top of stack"""
        peeked = self._stack.pop()
        # Only remove from shadow stack if we're
        # removing a 'local minimum' from the main stack
        if (peeked <= self._min_stack[-1]):
            self._min_stack.pop()
        return peeked

    def get_min(self):
        """Return min item or None if stack if empty"""
        if self._stack:
            return self._min_stack[-1]
        else:
            return None

    def __str__(self):
        return '\n'.join(map(str, self._stack[::-1]))


# Create and populate stack
s = Stack()
s.push(3)
s.push(4)
s.push(2)
s.push(2)
s.push(5)
s.push(0)
s.push(1)
s.push(4)
s.push(1)
print s  # [1, 4, 1, 0, 5, 2, 2, 4, 3]

assert s.get_min() == 0
s.pop()
s.pop()
s.pop()
assert s.get_min() == 0
s.pop()
assert s.get_min() == 2
s.pop()
s.pop()
assert s.get_min() == 2
print '\n', s
