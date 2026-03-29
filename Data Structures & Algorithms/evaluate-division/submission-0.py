class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        helper = collections.defaultdict(list)

        for (Ai, Bi), val in zip(equations, values):
            # Ai / Bi = val

            helper[Ai].append([Bi, val])
            helper[Bi].append([Ai, 1/val])

        ans = []
        visited = set()
        def dfs(top, bot, total):
            if top == bot:
                return total
            if top in visited:
                return -1
            ret = -1
            visited.add(top)
            for var, val in helper[top]:
                temp = dfs(var, bot, total*val)
                if temp != -1:
                    return temp
            visited.remove(top)
            #for var, val in helper[bot]:
            #    ret = dfs(top, var, total*val)
            return ret
            

        for top, bot in queries:
            visited = set()
            if top not in helper or bot not in helper:
                ans.append(-1)
            else:
                ans.append(dfs(top, bot, 1))
        return ans