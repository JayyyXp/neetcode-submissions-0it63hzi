class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        pos = deque()
        neg = deque()

        for n in nums:
            if not ans:
                if n > 0:
                    ans.append(n)
                else:
                    neg.append(n)
            else:
                if ans[-1] > 0:
                    if neg:
                        ans.append(neg.popleft())
                        if n > 0:
                            pos.append(n)
                        else:
                            neg.append(n)
                    elif n > 0:
                        pos.append(n)
                    else:
                        ans.append(n)
                else:
                    if pos:
                        ans.append(pos.popleft())
                        if n > 0:
                            pos.append(n)
                        else:
                            neg.append(n)
                    elif n > 0:
                        ans.append(n)
                    else:
                        neg.append(n)
        print(ans, pos, neg)
        if ans[-1] > 0:
            while True:
                if not neg:
                    break
                ans.append(neg.popleft())
                if not pos:
                    break
                ans.append(pos.popleft())
        else:
            while True:
                if not pos:
                    break
                ans.append(pos.popleft())
                if not neg:
                    break
                ans.append(neg.popleft())
        return ans 