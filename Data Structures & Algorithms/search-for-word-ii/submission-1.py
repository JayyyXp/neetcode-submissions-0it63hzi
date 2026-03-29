class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        wordStart = {}
        for i, word in enumerate(words):
            if word[0] in wordStart:
                wordStart[word[0]].append([i, word])
            else:
                wordStart[word[0]] = [[i, word]]
        print(wordStart)
        visited = set()
        def dfs(r,c, idx, wordIdx):
            if idx == len(words[wordIdx]):
                return True
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visited or
                board[r][c] != words[wordIdx][idx]
                ):
                return False
            #print(r,c,board[r][c],  idx, wordIdx)
            visited.add((r,c))
            ret = (
                dfs(r+1,c, idx+1, wordIdx) or
                dfs(r-1,c, idx+1, wordIdx) or
                dfs(r,c+1, idx+1, wordIdx) or
                dfs(r,c-1, idx+1, wordIdx)
            )
            visited.remove((r,c))
            return ret
            

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                letter = board[r][c]
                if letter in wordStart:
                    for i, (wordIdx, word) in enumerate(wordStart[letter]):
                        visited.clear()
                        #print('searching', word)

                        if wordIdx >= 0 and dfs(r,c,0, wordIdx):
                            wordStart[letter][i][0] = -1 
                            ans.append(word)
                        #print(wordStart)
                        #print(ans)
        return ans