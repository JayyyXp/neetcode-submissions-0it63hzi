class Solution:
    def compress(self, chars: List[str]) -> int:
        

        free_idx = 0
        prev = chars[0]
        group_len = 1
        ans = 0

        def update():
            nonlocal ans, free_idx
            ans += 1 
            chars[free_idx] = prev
            free_idx += 1

            if group_len > 1:
                for c in str(group_len):
                    chars[free_idx] = c
                    free_idx += 1
                    ans += 1

        for i in range(1, len(chars)):
            char = chars[i]
            if char == prev:
                group_len += 1
            else:
                update()
                prev = char
                group_len = 1 
        update()
        return ans