class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        curr = []
        curr_len = 0

        def format_to_string(l, l_len):
            if len(l) == 1:
                return l[0] + " " * (maxWidth - l_len)

            spaces = maxWidth - l_len
            slots = len(l) - 1
            each = spaces // slots
            extra = spaces % slots

            res = []
            for i in range(slots):
                res.append(l[i])
                space_count = each + (1 if extra > 0 else 0)
                if extra > 0:
                    extra -= 1
                res.append(" " * space_count)
            res.append(l[-1])  # append last word

            return "".join(res)

        for word in words:
            if curr_len + len(word) + len(curr) > maxWidth:
                ans.append(format_to_string(curr, curr_len))
                curr = [word]
                curr_len = len(word)
            else:
                curr.append(word)
                curr_len += len(word)

        # last line: left-justified
        if curr:
            line = " ".join(curr)
            line += " " * (maxWidth - len(line))
            ans.append(line)

        return ans
