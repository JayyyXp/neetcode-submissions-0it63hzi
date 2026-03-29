class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        helper = {}
        for s,e in edges:
            helper[s] = helper.get(s, []) + [e]
            helper[e] = helper.get(e, []) + [s]
        print(helper)

        def dfs(curr, start, visited):
            #print(curr, helper[curr], start, visited)

            if curr == start:
                #print('found', curr)
                return True
            
            ret = False
            for e in helper[curr]:
                uEdge = tuple(sorted([curr, e]))
                if uEdge not in visited:
                    visited.add(uEdge)
                    if dfs(e, start, visited):
                        ret = True
                        break
                    visited.remove(uEdge)
                #else:
                    #print('skipping', uEdge)
            return ret 


        for edge in edges:
            visited = set()   
            visited.add(tuple(sorted(edge)))
            if dfs(edge[1],edge[0],visited):
                print(edge, visited)
                for i in range(len(edges) -1, -1, -1):
                    uEdge = tuple(sorted(edges[i]))
                    if uEdge in visited:
                        return edges[i]