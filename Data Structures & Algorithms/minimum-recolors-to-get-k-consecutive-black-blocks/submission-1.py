class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        blocks = list(blocks)
        print(blocks)
        l = 0
        cur = 0
        mincol = len(blocks)
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                cur += 1
            while r - l + 1 > k:
                if blocks[l] == 'W':
                    cur -= 1
                l += 1
            if r - l + 1 == k:
                mincol = min(mincol, cur)
        return mincol