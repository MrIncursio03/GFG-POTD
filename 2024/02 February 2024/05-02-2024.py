"""

Author : Shuvam Kumar Singh
Date : 05/02/2024
Problem : Sorted insert for circular linked list
Difficulty : Medium

"""


class Solution:
    def sortedInsert(self, head, data):
        #code here
        class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

class Solution:
    def reverse(self, head):
        prev, cur = None, head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev

    def subtract(self, head1, head2):
        ans, second = LinkedList(), LinkedList()
        carry = 0

        while head1 or head2:
            cur = (head1.data if head1 else 0) - (head2.data if head2 else 0) - carry
            carry = cur < 0

            if carry:
                if (head1 and head1.next) or (head2 and head2.next):
                    ans.insert(10 + cur)
                    second.insert(0)
                else:
                    second.insert(abs(cur))
            else:
                ans.insert(cur)
                second.insert(0)

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        if carry:
            return second.head, ans.head
        else:
            return ans.head, None

    def subLinkedList(self, head1, head2):
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        res = self.subtract(head1, head2)
        final_ans = None

        if res[1]:
            head1, head2 = res[0], res[1]
            final_ans = self.subtract(head1, head2)[0]
        else:
            final_ans = res[0]

        final_ans = self.reverse(final_ans)

        while final_ans.data == 0 and final_ans.next:
            final_ans = final_ans.next

        return final_ans
