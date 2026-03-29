class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowConditions = {tuple(c) for c in rowConditions}
        colConditions = {tuple(c) for c in colConditions}

        if len(rowConditions) == k or len(colConditions) == k:
            return []
        def dfs(curr, adj,order):
            if curr in visiting:
                return True
            if curr in visited:
                return False
            visited.add(curr)
            visiting.add(curr)
            ret = False
            for nxt in adj.get(curr,[]):
                if dfs(nxt, adj,order):
                    ret = True
                    break
            visiting.remove(curr)
            order.append(curr)
            return ret

        adjRow = {n: [] for n in range(1,k+1)}
        rowInDegree = collections.defaultdict(int)
        for cS, cE in rowConditions:
            adjRow[cS].append(cE)
            rowInDegree[cE] += 1
        rowOrder = []
        visiting = set()
        visited = set()
        for n in adjRow:
            if rowInDegree[n] == 0:
                if dfs(n, adjRow,rowOrder):
                    print("cyckle")
                    return []
        rowOrder = rowOrder[::-1]
        print(rowOrder)

        adjCol = {n: [] for n in range(1,k+1)}
        colInDegree = collections.defaultdict(int)
        for cS, cE in colConditions:
            adjCol[cS].append(cE)
            colInDegree[cE] += 1
        colOrder = []
        visiting = set()
        visited = set()
        for n in adjCol:
            if colInDegree[n] == 0:
                if dfs(n, adjCol,colOrder):
                    print("cyckle")
                    return []
        colOrder = colOrder[::-1]
        print(colOrder)
        colOrder = {n:i for i,n in enumerate(colOrder)}

        ans = [[0]*k for _ in range(k)]

        for i, n in enumerate(rowOrder):
            ans[i][colOrder[n]] = n

        return ans

