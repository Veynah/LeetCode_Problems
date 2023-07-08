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

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return


# Testing
sol = Solution()

nums = [7, 4, 11, 15, 2]
target = 9

result = sol.twoSum(nums, target)

print(result)
