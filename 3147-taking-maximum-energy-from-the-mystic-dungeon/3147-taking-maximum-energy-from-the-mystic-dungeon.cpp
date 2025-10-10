class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        for(int i = 0; i < k; i++){
            for(int j = n-i-1; j >= k; j-= k){
                energy[j-k] += energy[j];
            }
        }
        int maxx = INT_MIN;
        for(int i = 0; i < n; i++){
            maxx = max(maxx, energy[n-i-1]);
        }
        return maxx;
    }
};