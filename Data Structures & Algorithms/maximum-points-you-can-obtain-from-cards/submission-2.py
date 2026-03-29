class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #li = cardPoints[-k:]+cardPoints[:k]
        #print(li)
        ans = 0
        s = 0
        l = 0     
        for r in range(2*k):

            if r - l + 1 == k:
                s += cardPoints[(len(cardPoints)-k+r)%len(cardPoints)]
                ans = max(ans,s)
                s -= cardPoints[(len(cardPoints)-k+l)%len(cardPoints)]
                l += 1
            else:
                s += cardPoints[(len(cardPoints)-k+r)%len(cardPoints)]
                ans = max(ans,s)
        return ans