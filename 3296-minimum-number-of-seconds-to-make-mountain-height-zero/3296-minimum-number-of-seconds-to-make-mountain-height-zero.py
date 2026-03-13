class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_reduce(total_time):
            reduced_height = 0
            for w in workerTimes:
                h = int((((1 + 8 * total_time / w)**0.5) - 1) / 2)
                reduced_height += h
                if reduced_height >= mountainHeight:
                    return True
            return reduced_height >= mountainHeight
        low = 1
        slowest = min(workerTimes)
        high = slowest * mountainHeight * (mountainHeight + 1) // 2    
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans