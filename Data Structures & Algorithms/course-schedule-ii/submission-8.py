class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        helper = defaultdict(list)
        courseToPreReqNum = {course: 0 for course in range(numCourses)}
        for nextCourse, preReq in prerequisites:
            helper[preReq].append(nextCourse)
            courseToPreReqNum[nextCourse] += 1

        
        coursesWithNoPreReq = []
        for course in range(numCourses):
            if courseToPreReqNum.get(course, 0) == 0:
                coursesWithNoPreReq.append(course)
        print('coursesWithNoPreReq', coursesWithNoPreReq)

        ans = []

        def dfs(course):
            if course in visited:
                print(visited, course)
                cyckleFound[0] = True
                return
            visited.add(course)
            for nextCourse in helper.get(course, []):
                dfs(nextCourse)
            temp.append(course)
            visited.remove(course)

        for course in coursesWithNoPreReq:
            temp = []
            visited = set()
            cyckleFound = [False]
            dfs(course)
            if cyckleFound[0]:
                return []
            ans += temp

        return ans[::-1]
