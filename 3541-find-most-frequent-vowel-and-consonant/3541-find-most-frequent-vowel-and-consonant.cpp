class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<int,int> co;
        unordered_map<int,int> vo;
        for(char ch: s){
            if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
                vo[int(ch)] += 1;
            }
            else{
            co[int(ch)] += 1;}
        }
        int ans_c = 0;
        int ans_v = 0;
        for(auto& pair: co){
            if(pair.second > ans_c){
                ans_c = pair.second;
            }
        }
        for(auto& pair: vo){
            if(pair.second > ans_v){
                ans_v = pair.second;
            }
        }
        return ans_c + ans_v;
    }
};