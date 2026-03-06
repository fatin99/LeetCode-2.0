# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # one-pass, 
    # When the first pointer (tail) reaches the end, the second pointer (nodeN) is exactly n nodes from the end
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        length = 0

        #second pointer (nodeN) is n nodes behind the first pointer (tail). 
        for _ in range(n):
            length += 1
            tail = tail.next                 
        nodeN = head

        # When the first pointer (tail) reaches the end, the second pointer (nodeN) is exactly n nodes from the end
        prev = None
        while tail:
            length += 1
            tail = tail.next
            prev = nodeN
            nodeN = nodeN.next

        if n >= length:
            if head.next:
                head = head.next
            else:
                head = None
            return head
        
        if not nodeN or not nodeN.next:
            prev.next = None
        else:
            prev.next = nodeN.next
        return head
    
    # # two-pass approach
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     tail = head
    #     length = 1
    #     while tail.next:
    #         length += 1
    #         tail = tail.next

    #     if n >= length:
    #         if head.next:
    #             head = head.next
    #         else:
    #             head = None
    #         return head
        
    #     nodeN = head
    #     prev = None

    #     for _ in range(length - n):
    #         prev = nodeN
    #         nodeN = nodeN.next
        
    #     if not nodeN or not nodeN.next:
    #         prev.next = None
    #     else:
    #         prev.next = nodeN.next
    #     return head
    
def list_to_linked_list(items):
    if not items:
        return None

    head = ListNode(items[0])
    current = head

    for value in items[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


lst = [1,2,3,4,5]
linked_list = list_to_linked_list(lst)
print(Solution().removeNthFromEnd(linked_list, 2))

lst = [1]
linked_list = list_to_linked_list(lst)
print(Solution().removeNthFromEnd(linked_list, 1))

lst = [1,2]
linked_list = list_to_linked_list(lst)
print(Solution().removeNthFromEnd(linked_list, 1))

lst = [1,2]
linked_list = list_to_linked_list(lst)
print(Solution().removeNthFromEnd(linked_list, 2))
print()       
        
        