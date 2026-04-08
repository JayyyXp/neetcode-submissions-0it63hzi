class Solution:
    def compress(self, chars: List[str]) -> int:
        free_idx = 0
        prev = chars[0]
        group_len = 1

        def update():
            nonlocal free_idx
            chars[free_idx] = prev
            free_idx += 1
            if group_len > 1:
                for c in str(group_len):
                    chars[free_idx] = c
                    free_idx += 1

        for i in range(1, len(chars)):
            if chars[i] == prev:
                group_len += 1
            else:
                update()
                prev = chars[i]
                group_len = 1
        update()
        return free_idx