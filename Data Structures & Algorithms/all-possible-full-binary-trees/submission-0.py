class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        

        def dfs(n):
            if n == 1:
                return [TreeNode(0)]
            if n % 2 == 0:
                return []
            ret = []
            for i in range(n):
                for left in dfs(i):
                    for right in dfs(n - 1 - i):
                        ret.append(
                            TreeNode(
                                0,
                                left,
                                right
                            )
                        )
            return ret
        return dfs(n)