class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        ans = []
        sentence = [] 
        def dfs(iS, iE):
            if iE >= len(s):
                # TODO only add valid ans
                if iS == iE: 
                    sen = " ".join(sentence)
                    ans.append(sen)
                return
            if s[iS:iE+1] in wordSet:
                # two choices
                sentence.append(s[iS:iE+1]) 
                dfs(iE+1, iE+1)
                sentence.pop() 
            # not add
            dfs(iS, iE+1)
            
        dfs(0,0)
        return ans