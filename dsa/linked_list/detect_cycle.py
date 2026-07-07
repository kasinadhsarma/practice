"""
Detect Cycle in a Linked List (Floyd's Algorithm)
----------------------------------------------------
Technique : Two pointers moving at different speeds ("tortoise and hare")
Idea      : Walk two pointers from the head — one advancing one node per
            step (slow), the other two nodes per step (fast). If the list
            has no cycle, fast reaches the end (None) first. If it DOES
            have a cycle, fast eventually laps slow inside the loop and
            they land on the same node — proving a cycle exists without
            needing any extra memory (no visited-set required).

Steps — has_cycle
    1. slow = fast = head
    2. While fast and fast.next are not None:
       a. slow = slow.next
       b. fast = fast.next.next
       c. If slow is fast: cycle found, return True.
    3. If the loop exits normally, there is no cycle.

Steps — find_cycle_start (once a cycle is confirmed)
    1. Run the same slow/fast loop until they meet.
    2. Reset one pointer to head; keep the other at the meeting point.
    3. Advance both one step at a time — where they meet again is the
       cycle's starting node. (This works because of the meeting-point
       distance math: distance from head to cycle start equals distance
       from meeting point back around to cycle start.)

Applications
    - Detecting corrupted/circular data structures
    - Interview staple demonstrating O(1)-space cycle detection

Time  Complexity : O(N)
Space Complexity : O(1) — only two pointers, no extra data structure
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class DetectCycle:
    @staticmethod
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    @staticmethod
    def find_cycle_start(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None  # no cycle

        pointer = head
        while pointer is not slow:
            pointer = pointer.next
            slow = slow.next
        return pointer


def build_list_with_cycle(values, cycle_index=None):
    """cycle_index: if given, list's tail.next points to node at that index."""
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index is not None and nodes and 0 <= cycle_index < len(nodes):
        nodes[-1].next = nodes[cycle_index]
    return nodes[0] if nodes else None


elements = list(map(int, input("enter elements separated by space: ").split()))
cycle_at = input("enter index to form a cycle back to (blank for no cycle): ").strip()
cycle_index = int(cycle_at) if cycle_at else None

head = build_list_with_cycle(elements, cycle_index)
print("has cycle:", DetectCycle.has_cycle(head))
