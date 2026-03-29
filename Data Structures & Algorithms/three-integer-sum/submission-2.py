class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(target, skipIdx):
            seen = collections.defaultdict(list)
            ans = []
            for i, n in enumerate(nums):
                if i != skipIdx:
                    if len(seen[n]) > 0:
                        ans.append([target-n, n])
                        seen[n].pop()
                    seen[target-n].append(i)
            return ans


        ans = set()
        for i, n in enumerate(nums):
            l = twoSum(-1 * n, i)
            for a in l:
                helper = [n] + a
                helper.sort()
                ans.add(tuple(helper))

        return [list(i) for i in ans ]