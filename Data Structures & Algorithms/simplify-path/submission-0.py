class Solution:
    def simplifyPath(self, path: str) -> str:
        h = path.split("/")
        print(h)
        s = []
        for p in h:
            if len(p) != 0:
                if p == "..":
                    if s:
                        s.pop()
                elif p == ".":
                    continue
                else:
                    s.append(p)
        print(s)
        ret = "/".join(s)
        print(ret)
        return "/" + ret