
class Solution(object):
    def oddEvenList(self, head):

        if not head:
            return None
        
        if not head.next:
            return head
        
        length =0
        t= head
        while t:
            prev=t
            length+=1
            t=t.next

        length = length//2

        print(length)
        print(prev.val)

        current = head
        node_to_move = head.next

        for _ in range(length):    
            current.next = node_to_move.next
            prev.next = node_to_move
            prev= prev.next
            prev.next=None
            current = current.next
            node_to_move =current.next

        
        return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def create_linked_list(self,values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def print_linked_list(self,head):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

# Example usage

values = [1, 3, 2, 5, 4]
ll = LinkedList()
head = ll.create_linked_list(values)
sol = Solution()
print("Original list:")
ll.print_linked_list(head)


new_head = sol.oddEvenList(head)
print("Odd Even list:")
ll.print_linked_list(new_head)
