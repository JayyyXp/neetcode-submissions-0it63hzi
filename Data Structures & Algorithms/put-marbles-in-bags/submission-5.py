class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        N = len(weights)
        
        cuts = []
        for i in range(N-1):
            cuts.append(
                weights[i]+weights[i+1]
            )
        cuts.sort()
        #rint(cuts)
        #print(cuts[-k+1:])
        #print(cuts[:k-1])
        return sum(cuts[-k+1:]) - sum(cuts[:k-1]) 