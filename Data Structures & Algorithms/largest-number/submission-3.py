class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        import functools 
        nums.sort(key=functools.cmp_to_key(lambda x,y: -1 if x+y > y+x else 1))
    
        return str(int("".join(nums)))