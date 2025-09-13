class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<int,int> co;
        unordered_map<int,int> vo;
        int ans_c = 0;
        int ans_v = 0;
        for(char ch: s){
            if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
                vo[int(ch)] += 1;
                ans_v = max(ans_v, vo[int(ch)]);
            }
            else{
            co[int(ch)] += 1;
            ans_c = max(ans_c, co[int(ch)]);
            }
        }
        return ans_c + ans_v;
    }
};