class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        #print(counter)
        buckets = [[] for _ in range(len(nums)+1)]
        #print(buckets)
        for n in counter:
            #print(n, counter[n])
            buckets[counter[n]].append(n)
            #print(buckets)
        ans = []
        print(buckets)
        for l in reversed(buckets):
            for n in l:
                ans.append(n)
            if len(ans) == k:
                break
        return ans