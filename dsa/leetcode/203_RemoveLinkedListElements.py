# https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


# Definition for singly-linked list.
from threading import currentThread


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
    # print(y)
    # while True:
    #     print(y.val)
    #     y = y.next
    #     if y == None:
    #         break
    return y


class Solution:
    def removeElements(self, head, val):
        if head == None:
            return head
        prev = head
        current = head
        op = current
        while True:
            if current.val == val:
                if current == op:
                    op = op.next
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
            
            if current == None:
                break
        return op



head = [1,2,6,3,4,5,6]
val = 6
head = makeLL(head)
obj = Solution()
op = obj.removeElements(head=head, val=val)
while op != None:
    print(op.val)
    op = op.next

