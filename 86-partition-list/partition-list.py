# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        left = ListNode(0)
        right = ListNode(0)

        leftTail = left
        rightTail = right

        while head:
            if head.val < x:
                leftTail.next = head
                leftTail = leftTail.next
            else:
                rightTail.next = head
                rightTail = rightTail.next

            head = head.next

        leftTail.next = right.next
        rightTail.next = None

        return left.next
        