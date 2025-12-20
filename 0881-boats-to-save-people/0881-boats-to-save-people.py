class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        i = 0
        j = n - 1
        count = 0
        while i <= j:
            s = people[i] + people[j]
            if s <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                count += 1
                j -= 1
        return count