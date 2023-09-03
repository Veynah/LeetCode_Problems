# https://leetcode.com/problems/valid-anagram/
from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """Function compares two strings and
        and determine if they're anagrams

        Args:
            s (string): string like "anagram"
            t (string): string like "nagaram"
            
        Output:
            boolean
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            # Since we don't know if the key s[i] exists in the hashmap
            # We use the function get this key and 0 is the default value
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
    
class Cheating:
    def cheatingAnagram(self, s, t):
        Counter(s) == Counter(t)
        