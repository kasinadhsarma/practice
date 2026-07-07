"""
Merge Two Sorted Linked Lists
--------------------------------
Technique : Two-pointer merge (same idea as the merge step of merge sort)
Idea      : Since both lists are already sorted, the smallest remaining
            head between the two lists is always at one of the two current
            positions. Repeatedly take whichever is smaller and attach it
            to the result — no need to look further ahead in either list.

Steps
    1. Use a dummy head node to avoid special-casing "is the result list
       empty yet".
    2. While both lists have nodes remaining:
       a. Compare the two current heads; attach the smaller to the result
          tail; advance that list's pointer.
    3. Once one list is exhausted, attach whatever remains of the other
       list directly (it's already sorted).

Applications
    - Merge step of merge sort, generalized to linked lists
    - Merging k sorted lists (repeatedly applying this pairwise, or with a
      heap — see dsa/heaps/)

Time  Complexity : O(N + M) — every node from both lists visited once
Space Complexity : O(1) extra — reuses existing nodes, only a dummy head
                   and a few pointers are allocated
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MergeTwoSortedLists:
    @staticmethod
    def merge(l1, l2):
        dummy = Node(None)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


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


a = sorted(map(int, input("enter first sorted list, space-separated: ").split()))
b = sorted(map(int, input("enter second sorted list, space-separated: ").split()))
merged = MergeTwoSortedLists.merge(build_list(a), build_list(b))
print("merged:", to_list(merged))
