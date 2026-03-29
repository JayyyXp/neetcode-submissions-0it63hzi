class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cache = set()
        def dfs(cand, t, chosen):
            if t == 0 and tuple(sorted(chosen)) not in cache:
                ans.append(chosen)

                cache.add(tuple(sorted(chosen)))
                return
            if t < 0:
                return
            for i, c in enumerate(cand):
                dfs(cand[:i] + cand[i+1:], t - c, chosen + [c])

            return

        
        dfs(candidates, target, [])

        return ans

        