"""
Problem: 83. Remove Duplicates from Sorted List
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list
Description: Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Difficulty: Easy
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return head
    
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head