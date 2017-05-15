class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next, pre = head, dummy
        while head:
            if head.val == val:
                pre.next, head = head.next, pre
            pre, head = head, head.next
        return dummy.next
