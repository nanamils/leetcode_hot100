# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. Initialize current node to dummy head of the returning list.
        # # 2. Initialize carry to 0.
        # # 3. Initialize p and q to head of l1 and l2 respectively.
        # # 4. Loop through lists l1 and l2 until you reach both ends.
        # #     4.1 Set x to node p's value. If p has reached the end of l1, set to 0.
        # #     4.2 Set y to node q's value. If q has reached the end of l2, set to 0.
        # #     4.3 Set sum = x + y + carry
        # #     4.4 Update carry = sum / 10
        # #     4.5 Create a new node with the digit value of (sum mod 10) and
        # #     set it to current node's next, then advance current node to next.
        # #     4.6 Advance both p and q.
        # # 5. Check if carry = 1, if so append a new node with digit 1 to the returning list.
        # # 6. Return dummy head's next node.
        # dummy = ListNode()
        # curr = dummy
        # carry = 0
        # while l1 or l2:
        #     x = l1.val if l1 else 0
        #     y = l2.val if l2 else 0
        #     s = x + y + carry
        #     carry = s // 10
        #     curr.next = ListNode(s % 10)
        #     curr = curr.next
        #     if l1: l1 = l1.next
        #     if l2: l2 = l2.next
        # if carry: curr.next = ListNode(1)
        # return dummy.next
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2:
            currSum = 0
            currSum += l1.val if l1 else 0
            currSum += l2.val if l2 else 0
            currSum += carry
            curr.next = ListNode(currSum % 10)
            curr = curr.next
            carry = currSum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry: curr.next = ListNode(1)
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(6)))
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next
