class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int MIN = INT_MAX;
        int n = nums.size();
        if(n == 1 || k == 1) return 0;
        sort(nums.begin(), nums.end());
        int i = 0 ,j = k;
        while(j <= n){
            long mx = nums[j-1];
            long mn = nums[i];
            long diff = mx - mn;
            if(diff < MIN) MIN = diff;
            i++;
            j++;
        }
        return MIN;
    }
};