class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        target = tickets[k]
        ans = 0
        for i, t in enumerate(tickets):
            if i <= k:
                ans += min(t, target)
            else:
                ans += min(t, target-1)
        return ans

        #i = 0
        #ans =  0
        #while tickets[k] != 0:
        #    if tickets[i] != 0:
        #       tickets[i] -= 1
        #        ans += 1
        #    i += 1
        #    i %= len(tickets) 
        #return ans