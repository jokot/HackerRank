"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

There is no input for this challenge. A random linked list is generated at runtime and passed to your function.
"""


def has_cycle(head):
    if head.next == None:
        return False
    return True