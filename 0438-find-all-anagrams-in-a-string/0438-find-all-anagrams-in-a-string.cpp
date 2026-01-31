class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n = s.size();
        int m = p.size();
        if(n < m) return {};
        vector<int> fqp(26, 0);
        vector<int> fqs(26, 0);
        for(int i = 0; i < m; i++){
            fqp[p[i] - 'a']++;
            fqs[s[i] - 'a']++;
        }
        vector<int> res;
        if(fqp == fqs) res.push_back(0);
        for(int i = m; i < n; i++){
            fqs[s[i] - 'a']++;
            fqs[s[i-m] - 'a']--;
            if(fqs == fqp) res.push_back(i-m+1); 
        }
        return res;
    }
};