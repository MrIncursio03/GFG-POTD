"""
Author : Shuvam Kumar Singh
Date : 01/02/2024
Problem : Panagram Checking
Difficulty : Easy
"""




class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        alphabet="abcdefghijklmnopqrstuvwxyz"
        s=s.lower()
        Flag=True
        for char in alphabet:
            if char not in s:
                Flag=False
        if (Flag==True):
            return 1
        else:
            return 0
