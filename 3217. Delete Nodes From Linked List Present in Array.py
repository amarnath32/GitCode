class Solution(object):

    def modifiedList(self, nums, head):
        if not head:
            return None
        
        seen = set(nums)

        prev= None
        current = head

        while current:
            if current.val in seen:
                if not prev:
                    head = current.next
                else:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current= current.next
                
        return head
        
        c = head
        while c:
            print(c.val,end ="->" if c.next else "\n")
            c=c.next

    
        



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
ll.create_list(10)
ll.printList()
a= Solution()
a.modifiedList([0,5,6],ll.head)
#a.printList()

