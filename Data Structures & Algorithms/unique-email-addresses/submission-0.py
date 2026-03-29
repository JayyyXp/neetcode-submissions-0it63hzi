class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ans = set()
        for email in emails:
            local_name, domain = email.split("@")

            tmp = []
            for c in local_name:
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    tmp.append(c)
            
            ans.add(
                "".join(tmp) + "@" + domain
            )
        return len(ans)