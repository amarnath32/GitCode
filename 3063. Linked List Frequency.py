# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def frequenciesOfElements(self, head):

        if not head:
            return None

        current = head
        freq = {}

        while current:
            if current.val in freq:
                freq[current.val] += 1
            else:
                freq[current.val] = 1
            current = current.next

        dummy = ListNode(0)
        dummy.next = None
        current1= dummy

        for key, value in freq.items():
             temp= ListNode(value)
             current1.next = temp
             temp.next = None
             current1 = current1.next

        current1 = dummy.next

        while current1:
            print(current1.val)
            current1=current1.next
    
            
        return dummy.next

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
arr = [1,1,2,1,2,3]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
print(sol.frequenciesOfElements(head))



arr = [1,1,2,2,2]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
print(sol.frequenciesOfElements(head))


arr = [6,5,4,3,2,1]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
print(sol.frequenciesOfElements(head))

arr = [1]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
print(sol.frequenciesOfElements(head))