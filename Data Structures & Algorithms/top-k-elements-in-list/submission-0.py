class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        ans = [(count, num) for num, count in counter.items()]
        ans = sorted(ans, reverse=True)
        print(ans)
        return [ans[i][1] for i in range(k)]