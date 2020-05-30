def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        finl_list = ListNode(0)
        curr = finl_list
        carry = 0
        while l1 or l2 or carry:
            if not l1:
                i = 0
            else:
                i = l1.val

            if not l2:
                j = 0
            else:
                j = l2.val     
            sum_all = i + j + carry

            if sum_all>=10:
                carry = 1
                remainder = sum_all%10
                curr.next = ListNode(remainder)
                curr = curr.next
            else:
                carry = 0
                curr.next = ListNode(sum_all)
                curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return finl_list.next