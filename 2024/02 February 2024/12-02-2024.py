"""

Author : Shuvam Kumar Singh
Date : 12/02/2024
Problem : Recursive sequence
Difficulty : Easy

"""


class Solution:
    def sequence(self, n):
        # code here
        ans=0
        MOD=7+(10**9)
        no=1
        for i in range(1,n+1):
            temp=1
            for j in range(i):
                temp=temp*no
                no+=1
            ans+=temp%MOD
        return ans%MOD
