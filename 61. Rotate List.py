# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        current = head

        if not head:
            return None
        
        if not head.next:
            return head

        def getLast(head):
            t = head
            while t.next:
                prev = t
                t= t.next
            return t,prev
        
        t1,prev = getLast(head)
        print(t1.val)

        for _ in range(3):
            t1,prev =getLast(head)
            dummy.next = t1
            t1.next = current
            prev.next = None
            head = dummy.next
            current = t1
        
        c= head
        while c:
            print(c.val, end = "->"if c.next else "\n")
            c= c.next
        print("\n")

        return head




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
ll.create_list(9)
ll.printList()
a= Solution()
a.rotateRight(ll.head,2)
#ll.printList()

        