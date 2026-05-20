class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n * k) time and O(1) space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head

        if len(lists) == 0:
            return None
        curr.next = lists[0]
        curr = curr.next

        for i in range(1, len(lists)):
            curr_list = lists[i]
            temp = head

            while curr_list and curr:
                if curr.val < curr_list.val:
                    temp.next = curr
                    curr = curr.next
                else:
                    temp.next = curr_list
                    curr_list = curr_list.next
                temp = temp.next

            temp.next = curr_list if curr_list else curr
            curr = head
            curr = curr.next

        return head.next

    # Divide And Conquer (Iteration)
    # O(nlogk) time and O(k) space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                head = ListNode(0)
                curr = head

                while l1 and l2:
                    if l1.val < l2.val:
                        curr.next = l1
                        l1 = l1.next
                    else:
                        curr.next = l2
                        l2 = l2.next
                    curr = curr.next
                curr.next = l1 if l1 else l2
                mergedLists.append(head.next)

            lists = mergedLists
        return lists[0]


def list_to_linked_list(items):
    if not items:
        return None

    head = ListNode(items[0])
    current = head

    for value in items[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = []
for list in lists:
    linked_list = list_to_linked_list(list)
    linked_lists.append(linked_list)
print(Solution().mergeKLists(linked_lists))
