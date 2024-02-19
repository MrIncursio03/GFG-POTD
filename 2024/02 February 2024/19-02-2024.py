"""

Author : Shuvam Kumar Singh
Date : 19/02/2024
Problem : Game with String
Difficulty : Medium

"""


class Solution:
    def minValue(self, s, k):
        # code here
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        freqs=list(d.values())
        freqs.sort()
        freqs=freqs[::-1]
        for i in range(k):
            freqs[0]-=1
            freqs.sort()
            freqs=freqs[::-1]
        val=0
        for i in freqs:
            val=val+(i**2)
        return val
