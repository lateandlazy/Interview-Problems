class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int ans = 0, i = 0, j = n - 1;
        while(i < j){
            int curr = min(height[i], height[j]);
            ans = max(ans, curr * (j - i));
            if(height[j] > height[i]) i++;
            else j--;
        }
        return ans;
    }
};