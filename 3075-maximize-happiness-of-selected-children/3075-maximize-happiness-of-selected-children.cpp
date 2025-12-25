class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        int n = happiness.size();
        sort(happiness.begin(), happiness.end());
        int i = 0, j = n - 1; 
        long long res = 0;
        while(k > 0){
            int x = happiness[j] - i;
            if(x <= 0) break;
            res += x;
            i++;
            j--;
            k--;
        }
        return res;
    }
};