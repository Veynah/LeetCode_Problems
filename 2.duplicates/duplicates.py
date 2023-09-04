# https://leetcode.com/problems/contains-duplicate/

# The first method we could use is a brute force method where we're going to compare every
# number to all the numbers in the array.
# Time complexity of O(n^2) and Memory complexity of O(1)


class Solution1:
    def containsDuplicate(self, nums):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# Second method is sorting the array and check if there are duplicates nearby
# Time complexity is O(nlogn) and Memory complexity is O(1)


class Solution2:
    def containsDuplicate(self, nums):
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


# Third method is to use a hash set in order to store the data and
# Compare the values in the array to the data stored in order to only
# go through the array once
# Time complexity of O(n) and Memory complexity of O(n)


class Solution3:
    def containsDuplicate(self, nums):
        hashset = set() # A set doesn't allow duplicates so it's a better solution to find them

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
