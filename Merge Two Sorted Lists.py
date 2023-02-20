# https://leetcode.com/problems/merge-two-sorted-lists/description/ 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        curr = mergedList = ListNode()
        # take the max between list1 and list2
        while list1 and list2:
            if list1.val < list2.val:
                curr.next, list1 = list1, list1.next
            else:
                curr.next, list2 = list2, list2.next
            curr = curr.next
        # take not None list
        if list1 or list2:
            curr.next = list1 if list1 else list2
        else:
            curr.next = list1
        return mergedList.next