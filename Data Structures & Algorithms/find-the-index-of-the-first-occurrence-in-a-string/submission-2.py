class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H, N = len(haystack), len(needle)
        if N > H:
            return -1

        MOD1, BASE1 = 10**9 + 7,  31
        MOD2, BASE2 = 10**9 + 9,  37

        def val(c):
            return ord(c) - ord('a') + 1

        pow1 = pow(BASE1, N - 1, MOD1)
        pow2 = pow(BASE2, N - 1, MOD2)

        hn1 = hn2 = hh1 = hh2 = 0
        for i in range(N):
            hn1 = (hn1 * BASE1 + val(needle[i]))   % MOD1
            hn2 = (hn2 * BASE2 + val(needle[i]))   % MOD2
            hh1 = (hh1 * BASE1 + val(haystack[i])) % MOD1
            hh2 = (hh2 * BASE2 + val(haystack[i])) % MOD2

        for i in range(H - N + 1):
            if hh1 == hn1 and hh2 == hn2:
                return i
            if i + N < H:
                hh1 = (hh1 - val(haystack[i]) * pow1) % MOD1
                hh1 = (hh1 * BASE1 + val(haystack[i + N]))  % MOD1
                hh2 = (hh2 - val(haystack[i]) * pow2) % MOD2
                hh2 = (hh2 * BASE2 + val(haystack[i + N]))  % MOD2

        return -1