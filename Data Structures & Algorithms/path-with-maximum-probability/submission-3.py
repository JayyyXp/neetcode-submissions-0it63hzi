class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        prob = [0.0] * n
        prob[start_node] = 1.0

        for _ in range(n):
            tmp = list(prob)
            for p,(s,e) in zip(succProb,edges):
                tmp[e] = max(tmp[e], prob[s]*p)
                tmp[s] = max(tmp[s], prob[e]*p)

            prob = tmp
        return prob[end_node]