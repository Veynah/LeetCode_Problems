#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::pmr::string> groupAnagrams(vector<string> &strs) {
    std::unordered_map<string, vector<string>> res;
    for (const auto &s : strs) {
      vector<int> count(26, 0);
      for (char c : s) {
        count[c - 'a']++;
      }
      string key = to_string(count[0]);
      for (int i = 1; i < 26; ++i) {
        key += ',' + to_string(count[i]);
      }
      res[key].push_back(s);
    }
    vector<vector<string>> result;
    for (counst auto &pair : res) {
      result.push_back(pair.second);
    }
    return result;
  }
};
