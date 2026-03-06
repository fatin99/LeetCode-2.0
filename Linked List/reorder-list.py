# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # Time: O(n)
    # Space: O(n)
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     nodeList = []
    #     tail = head
    #     while tail:
    #         nodeList.append(tail)
    #         tail = tail.next

    #     length = len(nodeList)
    #     curr = head

    #     while len(nodeList) > length / 2 + 1:
    #         tail = nodeList[-1]
    #         temp = curr.next
    #         curr.next = tail
    #         tail.next = temp
            
    #         curr = curr.next
    #         curr = curr.next
            
    #         nodeList.pop()

    #     if length / 2 + 1 == len(nodeList):
    #         curr = curr.next
    #         curr.next = None
    #     else:
    #         curr.next = None
    
    # Time: O(n^2)
    # Space: O(1)
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     tail = head
    #     length = 0
    #     while tail.next:
    #         length += 1
    #         tail = tail.next

    #     front = head
    #     back = tail
        
    #     currLength = length - 1
    #     while currLength > 0:
    #         temp = front.next
    #         front.next = back
    #         back.next = temp

    #         front = front.next
    #         front = front.next

    #         for _ in range(currLength):
    #             back = back.next
    #         currLength -= 2

    #     if currLength == 0:
    #         front.next = back
    #         back.next = None
    #     else:
    #         front.next = None
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tail = head
        mid = head
        while tail.next:
            mid = mid.next
            if tail.next:
                tail = tail.next
            if tail.next:
                tail = tail.next
        
        
        #reverse second half
        front2 = None
        while mid:
            temp = mid.next
            mid.next = front2
            front2 = mid
            mid = temp
        
        front1 = head        
        # combine first and second half
        while front2 and front1:
            temp1 = front1.next
            temp2 = front2.next
            front1.next = front2
            front2.next = temp1
            
            if temp2 and not temp1:                
                temp2.next = None
            if not temp2 and temp1:
                temp1.next = None
            front2 = temp2
            front1 = temp1
             
def list_to_linked_list(items):
    if not items:
        return None

    head = ListNode(items[0])
    current = head

    for value in items[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


lst = [1, 2, 3, 4, 5, 6]
linked_list = list_to_linked_list(lst)
print(Solution().reorderList(linked_list))

lst = [1, 2, 3, 4, 5]
linked_list = list_to_linked_list(lst)
print(Solution().reorderList(linked_list))

lst = [1,2,3,4]
linked_list = list_to_linked_list(lst)
print(Solution().reorderList(linked_list))
print()