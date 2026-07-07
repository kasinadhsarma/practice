"""
Doubly Linked List
--------------------
Technique : Chained nodes with BOTH a `next` and a `prev` pointer
Idea      : A singly linked list can only be walked forward, and deleting a
            known node still requires tracking its predecessor manually.
            Adding a `prev` pointer to every node makes backward traversal
            O(1) per step and lets a node be spliced out in O(1) once you
            already hold a reference to it (no need to search for `prev`).

Operations
    insert_at_head(val) / insert_at_tail(val)
        Same idea as the singly linked list, but also wire up `prev` on
        the neighbor, and a tail pointer is maintained for O(1) tail
        insertion (the main practical advantage over the singly list).
        Time: O(1)

    delete_value(val)
        Walk to find the node (O(N) to find it), then splice it out in
        O(1) by relinking its neighbors' `prev`/`next` directly.
        Time: O(N) to find + O(1) to unlink

    traverse_forward() / traverse_backward()
        Walk via `next` from head, or via `prev` from tail.
        Time: O(N)

Applications
    - Browser history (back/forward), text editor undo/redo
    - LRU cache implementation (O(1) move-to-front / evict-from-back)
    - Deque implementations

Time  Complexity : insert head/tail O(1)  |  delete O(N) (find) + O(1) (unlink)
Space Complexity : O(n) — two pointers per node
"""

class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val):
        node = DNode(val)
        if self.head is None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_tail(self, val):
        node = DNode(val)
        if self.tail is None:
            self.head = self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def delete_value(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return True
            curr = curr.next
        return False

    def traverse_forward(self):
        result, curr = [], self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def traverse_backward(self):
        result, curr = [], self.tail
        while curr:
            result.append(curr.val)
            curr = curr.prev
        return result


elements = list(map(int, input("enter elements to insert at tail, separated by space: ").split()))
dll = DoublyLinkedList()
for e in elements:
    dll.insert_at_tail(e)
print("forward  :", dll.traverse_forward())
print("backward :", dll.traverse_backward())
