# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:56:33 2020

@author: gabriel
"""
def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if(c in "abcdefghijklmnopqrstuvwxyz"):
                ans = ans + c
        return ans


    def isPal(s):
        print(s)
        if(len(s) <= 1):
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
        
    return isPal(toChars(s))            


print(isPalindrome("omississimo"))