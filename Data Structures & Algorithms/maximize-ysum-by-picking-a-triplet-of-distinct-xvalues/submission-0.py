class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        maxDict = collections.defaultdict(int)
        for i,j in zip(x,y):
            maxDict[i] = max(maxDict[i], j)
        if len(maxDict) < 3:
            return -1
        print(maxDict)
        ans = [0,0,0]
        
        for _, val in maxDict.items():
            if val > ans[0]:
                ans[0] = val
                ans.sort()
        return sum(ans)