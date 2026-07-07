"""
Singly Linked List
--------------------
Technique : Chained nodes, each holding a value and a pointer to the next
Idea      : Unlike an array, a linked list doesn't need contiguous memory —
            each Node points to the next one. This trades O(1) random
            access (arrays) for O(1) insertion/deletion at the head and no
            need to pre-allocate or resize.

Operations
    insert_at_head(val)
        New node's `next` = current head; head = new node.
        Time: O(1)

    insert_at_tail(val)
        Walk to the last node, attach the new node after it.
        Time: O(N) — no tail pointer kept here

    delete_value(val)
        Walk the list; when found, splice it out by pointing the previous
        node's `next` past it.
        Time: O(N)

    search(val)
        Walk the list comparing each node's value.
        Time: O(N)

    to_list()
        Walk the list collecting values, for easy inspection/testing.
        Time: O(N)

Applications
    - Building block for stacks, queues, hash-map buckets (chaining)
    - Any structure needing cheap head insertion/removal without shifting

Time  Complexity : insert_at_head O(1)  |  insert_at_tail/delete/search O(N)
Space Complexity : O(n) — one Node per element
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert_at_tail(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def delete_value(self, val):
        if self.head is None:
            return False
        if self.head.val == val:
            self.head = self.head.next
            return True
        prev, curr = self.head, self.head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return True
            prev, curr = curr, curr.next
        return False

    def search(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def length(self):
        count, curr = 0, self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def to_list(self):
        result, curr = [], self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


elements = list(map(int, input("enter elements to insert at tail, separated by space: ").split()))
sll = SinglyLinkedList()
for e in elements:
    sll.insert_at_tail(e)
print("list        :", sll.to_list())
print("length      :", sll.length())
sll.insert_at_head(0)
print("after insert_at_head(0):", sll.to_list())
