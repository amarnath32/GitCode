# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def gameResult(self, head):

        if not head: 
            return None

        even = head
        odd = head.next
        even_value = 0
        odd_value = 0

        while odd:
            if even.val > odd.val:
                print(even_value)
                even_value +=1
            else:
                odd_value +=1
            even = odd.next
            if not odd.next:
                break
            odd = odd.next.next

        if even_value == odd_value:
            return "Tie"

        return "Even" if even_value > odd_value else "Odd"
        
                

        
  

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
arr = [2,1]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
print(sol.gameResult(head))



arr = [2,5,4,7,20,5]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
print(sol.gameResult(head))


arr = [4,5,2,1]
head = sol.create_linked_list(arr)
print("Original list:")
sol.print_linked_list(head)
print(sol.gameResult(head))
