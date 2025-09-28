class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        unordered_map <int,int> fr;
        for(int num: nums){
            fr[num] += 1;
            if(fr[num] > 2) return false;
        }
        return true;
    }
};