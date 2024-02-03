"""

Author : Shuvam Kumar Singh
Date : 03/02/2024
Problem : Decimal Equivalent of Binary Linked List
Difficulty : Easy

"""

class Solution:
    def decimalValue(self, head):
        MOD = 1000000007
        ans = 0

        while head:
            ans = (ans * 2) % MOD
            ans = (ans + head.data) % MOD
            head = head.next

        return ans
