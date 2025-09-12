class Solution {
public:
    string sortVowels(string s) {
        vector<int> ascii;
        vector<int> index;
        for(int i = 0; i < s.size(); i++){
            char ch = s[i];
            if(ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' || ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
                ascii.push_back(int(ch));
                index.push_back(i);
            }
        }
        sort(ascii.begin(), ascii.end());
        for(int j = 0; j < index.size(); j++){
            char x = (char)ascii[j] ;
            s[index[j]] = x;
        }
        return s;
    }
};