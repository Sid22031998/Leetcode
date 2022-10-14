class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=1
        # to count the no of nodes
        while temp.next:
            count+=1
            temp=temp.next
        mid=count//2
        # print(count, mid)

        # base condition
        if mid==0:
            head=None
            return head
        count=1
        node=head
        while head:
            if count==mid:
                # print(head.val, head.next.val)
                head.next=head.next.next
            else:
                head=head.next
            count+=1
        return node
