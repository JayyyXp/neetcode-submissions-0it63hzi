class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        rog = {c: set() for w in words for c in w}

        # Build up the relative ordering graph
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word1), len(word2))
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                # Invalid case: prefix comes after
                return ""

            # word2 is always equal to word1 len or longer
            for j in range(len(word2)):
                if j == len(word1):
                    # case: 
                    # hrn
                    # hrny
                    # ????
                    break
                elif word1[j] != word2[j]:
                    # case: 
                    # hrn
                    # hry
                    rog[word1[j]].add(word2[j])
                    break
        
        print(rog)



        #if len(possible_starts) == 0 or len(possible_starts) == len(chars):
        #    print('no starts / all starts')
        #    return ''

        
        visited = set()
        visiting = set()
        output = []
        cycle = [False]

        def dfs(c):
            if c in visiting:
                cycle[0] = True
                return
            if c in visited:
                return
            visiting.add(c)
            for nei in rog[c]:
                dfs(nei)
            visiting.remove(c)
            visited.add(c)
            output.append(c)
            


        for c in rog:
            if c not in visited:
                dfs(c)
                if cycle[0]:
                    return ""
        
        return ''.join(reversed(output))
