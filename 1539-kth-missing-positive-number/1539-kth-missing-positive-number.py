class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        def check(x):
            low = 0
            high = n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == x:
                    return True
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    low = mid + 1
            return False 
        ans = -1               
        i = 1
        while k > 0:
            if check(i):
                i += 1
            else:
                k -= 1
                ans = i
                i += 1
        return ans 