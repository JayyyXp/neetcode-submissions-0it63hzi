class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        q = deque([['0000', 0]])

        while q:
            qLen = len(q)
            for i in range(qLen):
                curr, d = q.popleft()
                if curr == target:
                    return d
                if curr in deadends or curr in visited:
                    continue
                visited.add(curr)
                for i,wheel in enumerate(curr):
                    new_pos = int(curr[i])
                    
                    new_lock = curr[:i] + str((new_pos-1) % 10) + curr[i+1:]
                    q.append([new_lock, d+1])
                    
                    new_lock = curr[:i] + str((new_pos+1)% 10) + curr[i+1:]
                    q.append([new_lock, d+1])

        return -1