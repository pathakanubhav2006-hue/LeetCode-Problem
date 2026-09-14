# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        curr=head
        L=[]
        while curr is not None:
            L.append(curr.val)
            curr=curr.next
        i=0
        j=len(L)-1

        while i<j:
            if L[i]!=L[j]:
                return False
            i=i+1
            j=j-1


        return True
        


        
        