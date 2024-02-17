"""

Author : Shuvam Kumar Singh
Date : 17/02/2024
Problem : Does array represent Heap
Difficulty : Easy

"""

class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here            
        i=0
        while 2*i+1<n and 2*i+2<n:
            if arr[i]<arr[2*i+1] or arr[i]<arr[2*i+2]:
                return 0
            i+=1
        while 2*i+1<n:
            if arr[i]<arr[2*i+1]:
                return 0
            i+=1
        while 2*i+2<n:
            if arr[i]<arr[2*i+2]:
                return 0
            i+=1
        return 1

