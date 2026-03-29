class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wLen = len(beginWord)
        # pre-calculate the differences
        helper = {}
        for word1 in wordList + [beginWord]:
            for word2 in wordList + [beginWord]:
                if word1 == word2:
                    continue
                sameCount = 0
                for i in range(wLen):
                    if word1[i] == word2[i]:
                        sameCount += 1
                helper[(word1, word2)] = True if sameCount == wLen-1 else False

        print(helper) 
        ans = [float('inf')]
        visited = set()
        def dfs(currWord, count):
            if currWord in visited:
                return
            if currWord == endWord:
                ans[0] = min(ans[0], count)
                return
            visited.add(currWord)
            for word in wordList:
                if word == currWord:
                    continue
                if helper[(currWord, word)]:
                    dfs(word, count+1)
            visited.remove(currWord)

        dfs(beginWord, 0)
        if ans[0] == float('inf'):
            return 0
        return ans[0] +1