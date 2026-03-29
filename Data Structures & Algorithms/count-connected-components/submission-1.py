class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        helper = collections.defaultdict(list)
        for a, b in edges:
            helper[a].append(b)
            helper[b].append(a)

        ans = 0
        nodesVisited = set()
        usedEdges = set()
        def dfs(curr):

            
            for nextNode in helper[curr]:
                if (curr, nextNode) not in usedEdges:
                    nodesVisited.add(curr)
                    usedEdges.add((curr,  nextNode))
                    dfs(nextNode)
                    #usedEdges.remove((curr,  nextNode))
        for i in range(n):
            if i not in nodesVisited:
                ans += 1
                dfs(i)
        return ans