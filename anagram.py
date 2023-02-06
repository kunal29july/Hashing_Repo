'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''
'''
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #just we need to check this condition:
        # if char wich belong to S is also present in T and there freq is equal
        if len(s)!=len(t):
            return False
        memo1={}
        memo2={}
        for i in range (len(s)):
            if s[i] not in memo1:
                memo1[s[i]]=1
            else:
                memo1[s[i]]=memo1[s[i]]+1

        for j in range (len(t)):
            if t[j] not in memo2:
                memo2[t[j]]=1
            else:
                memo2[t[j]]=memo2[t[j]]+1

        for char in memo1:
            if char in memo2 and memo1[char]==memo2[char]:
                continue
            else:
                return False
        return True
