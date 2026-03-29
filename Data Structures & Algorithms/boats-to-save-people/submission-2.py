class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l, r = 0, len(people)-1
        ans = 0
        while l <= r:
            if people[r] == limit:
                r -= 1
                ans += 1
            elif people[r] + people[l] > limit:
                r -= 1
                ans += 1
            else:
                r -= 1
                l += 1
                ans += 1
        

        
        return ans

                    
