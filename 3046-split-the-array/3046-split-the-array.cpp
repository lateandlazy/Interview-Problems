class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        map<int,int> fr;
        for(int num: nums){
            fr[num]++;
            if(fr[num] > 2) return false;
        }
        return true;
    }
};