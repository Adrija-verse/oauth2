class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        new = temp
        
        extra = 0
        while l1 or l2 or extra:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + extra
            extra = val // 10
            val = val % 10
            new.next = ListNode(val)
            new = new.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temp.next
