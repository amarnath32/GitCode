# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def middleNode(self, head):

        if not head or not head.next:
            return None

        dummy= ListNode(0)
        dummy.next = head
        slow = head
        fast = head
        prev= head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return slow
        