# https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def reverseList(self, head):
        if head == None:
            return head
        l = []
        while head:
            l.insert(0, head.val)
            head = head.next
        return makeLL(l)
    

    def reverseList2(self, head):
        if head is None:
            return None
        prev , nxt = None , None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
    
    # recursive
    # https://leetcode.com/problems/reverse-linked-list/discuss/1939316/Python-recursive-solution-explanation-with-visualization.
    # https://www.youtube.com/watch?v=KYH83T4q6Vs
    def reverseList3(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return rest


head = [1,2,3,4,5]
head = makeLL(head)
obj = Solution()
op = obj.reverseList3(head)
while op:
    print(op.val, end=" ")
    op = op.next