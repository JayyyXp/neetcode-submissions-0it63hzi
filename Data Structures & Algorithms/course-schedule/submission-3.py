class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        helper = {}
        for a,b in prerequisites:
            helper[b] = helper.get(b, []) + [a] 
        print(helper)
        def dfs(start, course, visited):
            if course in visited:
                if start == course:
                    return False
                return True
            visited.add(course)
            ret = True
            if course in helper:
                for c in helper[course]:
                    ret = ret and dfs(start, c, visited)
            return ret
        for pre, after in helper.items():
            if not dfs(pre, pre, set()):
                return False
        return True
            #dfs(pre)
