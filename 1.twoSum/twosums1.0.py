# https://leetcode.com/problems/two-sum/
# First test is to understand how does the enumerate function work
# for i, value in enumerate(['apple', 'banana', 'mango', 'strawberry', 'coconut']):
#    print(i, value)
# Output:
# 0 apple
# 1 banana
# 2 mango
# 3 strawberry
# 4 coconut
# Then learn what are hash tables : https://en.wikipedia.org/wiki/Hash_table

# Exemples of what outputs we're looking for
#   Exemple 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#   Exemple 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

#   Exemple 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# import for type hinting
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}  # value : index
        """ Key-Value pairs

            In our case the key will be the integers of the array
            and the value will be the indices.
            Why the integers as the keys ?
            Because in Python checking for the existence of keys is much faster (O(1) average case)
            than checking for the existence of the values (O(n) average case). The dictionnaries 
            are optimized for key lookup
        """
        for i, n in enumerate(nums): # At each iteration, i will be the index of the number and n the number itself
            diff = target - n # diff is the integer we are looking for
            if diff in hashMap: # if diff is already in the hashMap, we return the index of the first number we found and this one
                return [hashMap[diff], i]
            hashMap[n] = i # we add the number n as the key to our hashmap with the i as it's value
        return


# Testing
sol = Solution()

nums = [7, 4, 11, 15, 2]
target = 9

result = sol.twoSum(nums, target)

print(result)
