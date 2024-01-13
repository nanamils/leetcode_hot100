# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast.next:
            fast = fast.next
            gcd = self.gcd(slow.val, fast.val)
            slow.next = ListNode(gcd, slow.next)
            slow = slow.next.next
        return head


if __name__ == '__main__':
    l1 = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
    sol = Solution()
    sol.insertGreatestCommonDivisors(l1)
    while l1:
        print(l1.val)
        l1 = l1.next
