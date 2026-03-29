class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        personTrusts = collections.defaultdict(set)
        othersTrust = collections.defaultdict(set)
        for ai, bi in trust:
            personTrusts[ai].add(bi)
            othersTrust[bi].add(ai)
        
        cand = []
        for p in range(0, n+1):
            # 1.The town judge trusts nobody.
            if len(personTrusts[p]) == 0:
                # 2. Everybody (except for the town judge) trusts the town judge.
                if len(othersTrust[p]) == n -1:
                    cand.append(p)
        if len(cand) == 1:
            return cand[0]
        return -1

        