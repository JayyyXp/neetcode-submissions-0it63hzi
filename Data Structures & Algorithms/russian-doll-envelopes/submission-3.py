class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        wSort = sorted(envelopes, key=lambda x: -x[0])
        hSort = sorted(envelopes, key=lambda x: -x[1])
        memo = {}
        def dfs(maxIdx, i, listRef):
            if i == len(envelopes):
                return 0
            if (maxIdx, i, listRef) in memo:
                return memo[(maxIdx, i, listRef)]
            if listRef == "H":
                useList = hSort
            else:
                useList = wSort

            ret = dfs(maxIdx, i+1, listRef)
            if useList[maxIdx][0] > useList[i][0] and useList[maxIdx][1] > useList[i][1]:
                ret = max(
                    1 + dfs(i, i+1, listRef),
                    ret,
                )
            memo[(maxIdx, i, listRef)] = ret
            return ret
    
        return max(dfs(0,1,"H"), dfs(0,1,"W")) + 1