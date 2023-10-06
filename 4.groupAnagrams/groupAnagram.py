# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        hashMap = defaultdict(list) # Using a defaultdict in case there is an edge case

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)
        return hashMap.values()
