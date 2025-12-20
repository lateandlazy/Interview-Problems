class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs[0].size();
        int m = strs.size();
        int res = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m-1; j++){
                if((int)strs[j][i] > (int)strs[j+1][i]){
                    res++;
                    break;
                }
            }
        }
        return res;
    }
};