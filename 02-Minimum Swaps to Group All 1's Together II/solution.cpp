#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        int count = accumulate(nums.begin(), nums.begin() + total, 0);
        int res = count;


        for (int i = total; i < nums.size() + total; ++i) {
            count += nums[i % nums.size()] - nums[(i - total + nums.size()) % nums.size()];
            res = max(res, count);
        }
        return total - res;
    }
};