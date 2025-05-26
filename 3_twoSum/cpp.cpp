#include <unordered_map>
#include <vector>
class Solution {
public:
  std::vector<int> twoSum(vector<int> &nums, int target) {
    int n = nums.size();
    std::unordered_map<int, int> prevMap;

    for (int i = 0; i < n; i++) {
      int diff = target - nums[i];
      if (prevMap.find(diff) != prevMap.end()) {
        return {prevMap[diff], i};
      }
      prevMap.insert({nums[i], i});
    }
    return {};
  }
};
