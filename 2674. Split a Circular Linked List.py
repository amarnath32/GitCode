# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitCircularLinkedList(self, list):
        """
        :type list: Optional[ListNode]
        :rtype: List[Optional[ListNode]]
        """
        # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitCircularLinkedList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[Optional[ListNode]]
        """
        slow = head
        fast = head
        while fast.next != head and fast.next.next != head:
            slow = slow.next
            fast = fast.next.next

        if fast.next!= head:
            fast = fast.next    


        print(slow.val, fast.val)
        temp = slow.next
        slow.next = head
        fast.next = temp

        return head, temp
   

def create_circular_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    current.next = head  # Make the list circular
    return head

def print_circular_linked_list(head, length):
    current = head
    for _ in range(length):
        print(current.val, end=" -> ")
        current = current.next
    print("... (circular)")

# Example usage
sol = Solution()
arr = [1, 5,7]
head = create_circular_linked_list(arr)
print("Original circular linked list:")
print_circular_linked_list(head, len(arr))

head1, head2 = sol.splitCircularLinkedList(head)
print("First half of the circular linked list:")
print_circular_linked_list(head1, len(arr) // 2)
print("Second half of the circular linked list:")
print_circular_linked_list(head2, len(arr) - len(arr) // 2)

arr = [1,2,3,4,5,6]
head = create_circular_linked_list(arr)
print("Original circular linked list:")
print_circular_linked_list(head, len(arr))

head1, head2 = sol.splitCircularLinkedList(head)
print("First half of the circular linked list:")
print_circular_linked_list(head1, len(arr) // 2)
print("Second half of the circular linked list:")
print_circular_linked_list(head2, len(arr) - len(arr) // 2)