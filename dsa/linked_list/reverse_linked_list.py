"""
Reverse a Linked List
-----------------------
Technique : Iterative pointer rewiring, and recursive unwind
Idea      : Reversing means every node's `next` should point to what used
            to be BEFORE it. Walking forward while re-pointing `next`
            backward, one node at a time, does this in a single pass with
            no extra memory beyond a few pointers.

Iterative Steps
    1. Keep three pointers: prev (starts None), curr (starts at head),
       and a temporary next_node.
    2. While curr is not None:
       a. next_node = curr.next   (save it before overwriting)
       b. curr.next = prev        (reverse this link)
       c. prev = curr; curr = next_node   (advance both)
    3. prev is now the new head.

Recursive Idea
    Reverse everything after the current node first (recursion handles
    that), then fix this node's link: make the rest of the list point
    back to it, and point this node's `next` to None (it becomes the new
    tail).

Applications
    - Palindrome-check on a linked list (reverse the second half, compare)
    - Any "reverse in groups of k" style interview variant

Time  Complexity : O(N) — visits every node once, both approaches
Space Complexity : Iterative O(1)  |  Recursive O(N) — call stack depth
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class ReverseLinkedList:
    @staticmethod
    def reverse_iterative(head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    @staticmethod
    def reverse_recursive(head):
        if head is None or head.next is None:
            return head
        new_head = ReverseLinkedList.reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


elements = list(map(int, input("enter elements separated by space: ").split()))
head = build_list(elements)
reversed_head = ReverseLinkedList.reverse_iterative(head)
print("reversed (iterative):", to_list(reversed_head))

head = build_list(elements)
reversed_head = ReverseLinkedList.reverse_recursive(head)
print("reversed (recursive):", to_list(reversed_head))
