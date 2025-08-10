# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def create_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def print_linked_list(self, head):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

# Example usage
sol = Solution()
arr = [1, 1, 2, 3, 3]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
new_head = sol.deleteDuplicates(head)
print("List after removing duplicates:")
sol.print_linked_list(new_head)

arr = [1, 1, 2]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
new_head = sol.deleteDuplicates(head)
print("List after removing duplicates:")
sol.print_linked_list(new_head)