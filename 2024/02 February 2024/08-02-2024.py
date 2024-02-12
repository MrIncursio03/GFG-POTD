"""

Author : Shuvam Kumar Singh
Date : 08/02/2024
Problem : Check if all leaves are at same level
Difficulty : Easy

"""


class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        if not root:
            return True
        
        prevlvl = -1
        q=deque([[root,0]])
        
        while(q):
            for i in range(len(q)):
                node, lvl = q.popleft()
                if not node:continue
                if (not node.left) and (not node.right):
                    
                    if prevlvl == -1:
                        prevlvl = lvl
                        
                    if prevlvl!=lvl:
                        return False
                        
                    continue
                
                q.append([node.left,lvl+1])
                q.append([node.right,lvl+1])
        return True
