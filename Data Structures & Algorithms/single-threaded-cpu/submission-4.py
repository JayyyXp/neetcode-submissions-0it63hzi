class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[e,p,i] for i,(e,p) in enumerate(tasks)]
        inSchedule = []
        heapq.heapify(tasks)
        ans = []
        t = tasks[0][0]
        while tasks or inSchedule:
            #print(t)
            while tasks and tasks[0][0] <= t:
                _, p,i = heapq.heappop(tasks)
                heapq.heappush(inSchedule, [p,i])
            #print(inSchedule)
            if inSchedule:
                p, i = heapq.heappop(inSchedule)
                ans.append(i)
                t += p
            else:
                t = tasks[0][0]
        return ans