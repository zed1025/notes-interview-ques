# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        l = list(set(l))
        l.sort()
        return self.makeLL(l)

    def makeLL(self, l):
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


head = [1,1,2,3,3]
obj = Solution()
head = obj.makeLL(head)
op = obj.deleteDuplicates(head)
while op:
    print(op.val)
    op = op.next
