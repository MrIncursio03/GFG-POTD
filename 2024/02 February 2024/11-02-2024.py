"""

Author : Shuvam Kumar Singh
Date : 11/02/2024
Problem : Recamans sequence
Difficulty : Easy

"""


class Solution:
    def recamanSequence(self, n):
        # code here
        res = [0]
        hashSet = set([0])
        for i in range(1,n+1):
            tmp = res [-1] - i 
            if tmp < 0 or tmp in hashSet:
                curTmp = res[-1] + i
                res.append(curTmp)
                hashSet.add(curTmp)
            else:
                res.append(tmp)
                hashSet.add(tmp)
        return res
