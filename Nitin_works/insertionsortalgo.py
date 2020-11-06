#Python3 Code:

# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None: return None
        pH = ListNode(-1)
        pH.next = head
        curr = head.next
        head.next = None
        sEnd = head
        
        while curr != None:
            nextCurr = curr.next
            if sEnd.val <= curr.val:
                sEnd.next = current
                curr.next = None
                sEnd = curr
            else:
                hSrtd = pH
                while hSrtd.next.val < curr.val:
                    hSrtd = hSrtd.next
                curr.next = hSrtd.next
                hSrtd.next = curr
            curr = nextCurr
        return pH.next