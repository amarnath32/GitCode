class Solution(object):
    def removeElements(self, head, val):

        if not head or not head.next:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current =current.next
        return dummy.next



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def new_node(self, value):
        return ListNode(value)

    def create_list(self, nums=0):
        self.head = self.new_node(0)
        current = self.head
        for i in range(1,nums):
            temp = self.new_node(i)
            current.next = temp
            current =current.next

    def printList(self):
        c = self.head
        while c:
            print(c.val,end ="->" if c.next else "\n")
            c=c.next


ll = LinkedList()
ll.create_list(11)
ll.printList()
a= Solution()
a.removeElements(ll.head,0)
ll.printList()