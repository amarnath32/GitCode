# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):

        length =0
        
        t= head
        while t:
            length+=1
            t = t.next

        ans =[None]*k
        j=0

        print(length)

        split_size = length//k
        remaining_part = length%k
        print(split_size,remaining_part)

        current = head
        prev=  current

        for j in range(k):
            new_part = current
            current_size = split_size
            if remaining_part >0:
                current_size+=1
                remaining_part-=1
            
            i=0
            while i<current_size:
                prev= current
                if current is not None:
                    current = current.next
                i+=1
            
            if prev is not None:
                prev.next = None


            ans[j] = new_part
    
        return ans


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
a.splitListToParts(ll.head,3)
ll.printList()