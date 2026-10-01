# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_gcd(self, a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        if not head or not head.next:
            return head
        
        curr = head
        
        while curr and curr.next:
            a=curr.val
            b=curr.next.val
            while b:
                a, b = b, a % b

            # 1. Calculate GCD using our custom function
            gcd_val = a
            new_node = ListNode(gcd_val)
            
            # 2. Link new node to the second node
            new_node.next = curr.next
            
            # 3. Link first node to the new node
            curr.next = new_node
            
            # 4. Advance curr past the new node to the next pair
            curr = new_node.next
            
        return head
        