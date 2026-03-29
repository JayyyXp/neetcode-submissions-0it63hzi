class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict

        # Create a helper to figure out 
        # from node X all nodes Y_0, Y_1,... Y_n 
        # we can get to
        helper = defaultdict(list)
        for s, e in edges:
            helper[s].append(e)
            helper[e].append(s)
        print(helper)    

        # helper var to keep track if from one node
        # we can get to all other nodes
        canGetToAll = False


        cache = {}

        def dfs(curr):
            # - if we got to end without a cyckle 
            # return True 
            # - otherwise 
            # return False
            #if not curr:
            #    cache[curr] = True
                #return True
            if curr in seen:
                cache[curr] = False
                return False
            if curr in cache:
                return cache[curr]
            seen.add(curr)
            res = True
            for e in helper[curr]:
                # Do not use the same edge twice
                # ie. do not go back on itself
                if (curr, e) in edgesUsed:
                    continue
                edgesUsed.add((curr, e))
                edgesUsed.add((e, curr))
                if not dfs(e):
                    res = False
            cache[curr] = res
            return res


        for node in range(n):
            seen = set()
            edgesUsed = set()
            if not dfs(node):
                return False
            if len(seen) == n:
                canGetToAll = True
        
        return canGetToAll