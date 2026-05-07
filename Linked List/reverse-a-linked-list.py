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


a = ListNode(val=5)
b = ListNode(val=4, next=a)
c = ListNode(val=3, next=b)
d = ListNode(val=2, next=c)
e = ListNode(val=1, next=d)
print(Solution().reverseList(e))
