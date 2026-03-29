class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def combinations2(total_n):
            if total_n < 0:
                return 0
            # This is (total_n + 2) choose 2
            return (total_n + 2) * (total_n + 1) // 2

        # PIE Formula:
        # + Total ways
        # - (3 choose 1) * ways where 1 child exceeds limit
        # + (3 choose 2) * ways where 2 children exceed limit
        # - (3 choose 3) * ways where 3 children exceed limit
        
        L = limit + 1
        ans = combinations2(n)             # Total
        ans -= 3 * combinations2(n - L)    # Sub 1 violation
        ans += 3 * combinations2(n - 2*L)  # Add 2 violations
        ans -= 1 * combinations2(n - 3*L)  # Sub 3 violations
        
        return ans