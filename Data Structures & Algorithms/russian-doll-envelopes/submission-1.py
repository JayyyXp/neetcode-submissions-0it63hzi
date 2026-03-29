class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        wSort = sorted(envelopes, key=lambda x: -x[0])
        hSort = sorted(envelopes, key=lambda x: -x[1])
        currW = wSort[0][0]
        currH = wSort[0][1]
        print(wSort)
        print(hSort)
        def dfs(maxIdx, i, listRef):
            if i == len(envelopes):
                return 0
            ret = 0
            if listRef[maxIdx][0] > listRef[i][0] and listRef[maxIdx][1] > listRef[i][1]:
                ret = max(
                    1 + dfs(i, i+1, listRef),
                    dfs(maxIdx, i+1, listRef),
                )
            else:
                ret = dfs(maxIdx, i+1, listRef)
            return ret
    
        return max(dfs(0,1,hSort), dfs(0,1,wSort)) + 1