# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # currNode = head
        # nodes = []
        # count = 0
        # while currNode:
        #     nodes.append(currNode)
        #     currNode = currNode.next
        #     count += 1
        # if count == 1:
        #     return nodes[-1]
        # if count == 0:
        #     return None
        # for i in range(count):
        #     index = len(nodes) - 1 - i
        #     currNode = nodes[index]
        #     if index > 0:
        #         currNode.next = nodes[index - 1]
        #     else:
        #         currNode.next = Nones
        # return nodes[-1]

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Attach remaining nodes (only one list will have remaining nodes)
        curr.next = list1 if list1 else list2
        
        return dummy.next
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # nodeMap = {}
        # while head:
        #     if head in nodeMap:
        #         return True
        #     nodeMap[head] = True
        #     head = head.next
        # return False
    
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



a = ListNode(val=9)
b = ListNode(val=7, next=a)
c = ListNode(val=5, next=b)
d = ListNode(val=3, next=c)
e = ListNode(val=1, next=d)
f = ListNode(val=10)
g = ListNode(val=8, next=f)
h = ListNode(val=6, next=g)
i = ListNode(val=4, next=h)
j = ListNode(val=2, next=i)
print(Solution().hasCycle(e))