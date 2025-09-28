class Solution {
public:
    vector<int> decimalRepresentation(int n) {
        vector<int> ans;
        long long power = 1;
        while(n > 0){
            long long d = n % 10;
            if(d > 0){
                long long temp = d * power;
                ans.push_back(temp);
            }
            n = n / 10;
            power = power * 10;    
        }
        reverse(ans.begin(), ans.end()); 
        return ans;
    }
};