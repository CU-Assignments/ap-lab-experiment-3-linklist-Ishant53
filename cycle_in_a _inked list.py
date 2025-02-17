from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Example usage
def create_cycle_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]  # Create cycle
    return nodes[0]


solution = Solution()
head = create_cycle_list([3, 2, 0, -4], 1)
print(solution.hasCycle(head))  # Output: True

head = create_cycle_list([1, 2], 0)
print(solution.hasCycle(head))  # Output: True

head = create_cycle_list([1], -1)
print(solution.hasCycle(head))  # Output: False
