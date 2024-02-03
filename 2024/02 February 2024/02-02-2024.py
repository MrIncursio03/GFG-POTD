"""

Author : Shuvam Kumar Singh
Date : 02/02/2024
Problem : Implement Atoi
Difficulty : Medium

"""


class Solution:
    def atoi(self, s: str) -> int:
        ans = 0
        sign = 1
        n = len(s)

        for i in range(n):
            if s[i] == '-' and i == 0:
                sign = -1
            elif '0' <= s[i] <= '9':
                ans = ans * 10 + int(s[i])
            else:
                return -1

        ans *= sign
        return ans
