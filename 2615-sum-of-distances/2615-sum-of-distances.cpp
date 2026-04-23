class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = nums.size();
        vector<long long> ans(n, 0);
        unordered_map<int, long long> count_map, sum_map;
        for (int i = 0; i < n; i++) {
            int val = nums[i];
            ans[i] += (count_map[val] * i) - sum_map[val];
            count_map[val]++;
            sum_map[val] += i;
        }
        count_map.clear();
        sum_map.clear();
        for (int i = n - 1; i >= 0; i--) {
            int val = nums[i];
            ans[i] += sum_map[val] - (count_map[val] * i); 
            count_map[val]++;
            sum_map[val] += i;
        }
        return ans;
    }
};