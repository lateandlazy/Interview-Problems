class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size();
        int m = s2.size();
        if(m < n)return false;
        vector<int> fqS1(26, 0);
        vector<int> fqS2(26, 0);
        for(int i = 0; i < n; i++){
            fqS1[s1[i] - 'a']++;
            fqS2[s2[i] - 'a']++;
        }
        if(fqS1 == fqS2) return true;
        for(int i = n; i < m; i++){
            fqS2[s2[i] - 'a']++;
            fqS2[s2[i-n] - 'a']--;
            if(fqS1 == fqS2) return true;
        }
        return false;
    }
};