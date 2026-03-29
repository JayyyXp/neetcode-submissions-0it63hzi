class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        accIdxToEmail = collections.defaultdict(list)
        emailToaccIdx = collections.defaultdict(list)
        for i, acc in enumerate(accounts):

            for j in range(1,len(acc)):
                accIdxToEmail[i].append(acc[j])
                emailToaccIdx[acc[j]].append(i)

        print(accIdxToEmail)
        print(emailToaccIdx)

        visited = set()
        def dfs(idx):
            if idx in visited:
                return
            print(idx)
            visited.add(idx)
            for email in accIdxToEmail[idx]:
                helper.add(email)
                for newIdx in emailToaccIdx[email]:
                    dfs(newIdx)
            #visited.remove(idx)

        ans = []
        for i, (name, *_) in enumerate(accounts):
            if i in visited:
                continue 
            helper = set()
            #visited = set()
            dfs(i)
            helper = list(helper)
            helper.sort()
            helper = [name] + helper
            ans.append(helper)
        return ans