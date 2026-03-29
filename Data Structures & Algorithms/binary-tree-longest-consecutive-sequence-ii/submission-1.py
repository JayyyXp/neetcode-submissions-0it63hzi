class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr):
            if not curr:
                return (0, 0)  # (increasing sequence, decreasing sequence)
            
            inc, dec = 1, 1  # Every node by itself is a sequence of length 1
            
            # Recursively find the longest increasing and decreasing sequences
            left_inc, left_dec = dfs(curr.left)
            right_inc, right_dec = dfs(curr.right)
            
            # Check if we can extend the increasing sequence
            if curr.left and curr.val + 1 == curr.left.val:
                inc = max(inc, left_inc + 1)
            # Check if we can extend the decreasing sequence
            if curr.left and curr.val - 1 == curr.left.val:
                dec = max(dec, left_dec + 1)

            # Check the same for the right child
            if curr.right and curr.val + 1 == curr.right.val:
                inc = max(inc, right_inc + 1)
            if curr.right and curr.val - 1 == curr.right.val:
                dec = max(dec, right_dec + 1)
                
            # Update the global max length: both increasing + decreasing sequences at the current node
            self.max_len = max(self.max_len, inc + dec - 1)
            
            return (inc, dec)

        # Initialize the global variable to track the maximum length
        self.max_len = 0
        
        # Start DFS from the root
        dfs(root)
        
        return self.max_len
