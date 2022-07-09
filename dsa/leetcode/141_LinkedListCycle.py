# https://leetcode.com/problems/linked-list-cycle/
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def makeLL(l):
    t = len(l)
    if len(l) == 0:
        return ListNode(None, None)
    x = ListNode(l[0], None)
    y = x
    for i in range(1, t):
        temp = ListNode(l[i], None)
        x.next = temp
        x = temp
    return y


class Solution:
    # https://leetcode.com/problems/linked-list-cycle/discuss/2240153/Thinking-Process-Explained-Also-Visualized-Enjoy-%3A)
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # https://leetcode.com/problems/linked-list-cycle/discuss/2245054/Simple-O(1)-space-solution-Python
    def hasCycle2(self, head):
        curr = head
        while curr:
            if curr.val == "#":
                return True
            curr.val = "#"
            curr = curr.next
        return False

