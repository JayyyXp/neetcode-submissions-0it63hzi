class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        N = len(heights)
        helper = deque([heights[-1]])
        for i in range(N-2, -1, -1):
            if heights[i] > helper[0]:
                helper.appendleft(heights[i])
            else:
                helper.appendleft(helper[0])
        print(heights)
        print(list(helper)[1:])
        ans = []
        for i in range(N-1):
            if heights[i] > helper[i+1]:
                ans.append(i) 
        return ans + [N-1]
