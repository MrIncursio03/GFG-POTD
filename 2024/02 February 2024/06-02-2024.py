"""

Author : Shuvam Kumar Singh
Date : 06/02/2024
Problem : Count the nodes at distance K from leaf
Difficulty : Medium

"""


class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        #code here
        res=set()
        def solve(root,l,ans):
            if root==None:
                return 
            if root.left==None and root.right==None:
                if ans-k==len(l):
                    res.add(root)
                elif ans-k<0 or ans-k>len(l):
                    return
                else:
                    res.add(l[ans-k])
            solve(root.left,l+[root],ans+1)
            solve(root.right,l+[root],ans+1)
        solve(root,[],0)
        return len(res)
