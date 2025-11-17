import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hp = []
        for num in nums:
            heapq.heappush(hp, num)
            if len(hp) > k: heapq.heappop(hp)
        #x = n - k
        return hp[0]