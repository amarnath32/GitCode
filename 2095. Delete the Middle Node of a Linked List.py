class Solution(object):
    def deleteMiddle(self, head):
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

        prev.next = slow.next
        
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
ll.create_list(9)
ll.printList()
a= Solution()
a.deleteMiddle(ll.head)
ll.printList()
