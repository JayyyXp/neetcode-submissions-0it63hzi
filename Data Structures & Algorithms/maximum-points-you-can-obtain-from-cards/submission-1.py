class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        li = cardPoints[-k:]+cardPoints[:k]
        print(li)
        ans = 0
        s = 0
        l = 0     
        for r in range(2*k):
            if r - l + 1 == k:
                s += li[r]
                ans = max(ans,s)
                s -= li[l]
                l += 1
            else:
                s += li[r]
                ans = max(ans,s)
        return ans