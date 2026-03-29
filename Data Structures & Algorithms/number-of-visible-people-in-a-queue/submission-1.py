class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []
        stack = []  # A stack to maintain the people that the current person can see
        for h in reversed(heights):  # Traverse from right to left
            count = 0
            # While there are people in the stack and the current height is greater than the top of the stack
            while stack and stack[-1] <= h:
                stack.pop()  # Pop people that are shorter or equal to the current person
                count += 1  # These people are visible to the current person
            if stack:  # If there's someone taller in the stack, this person can see one more
                count += 1
            stack.append(h)  # Add the current person to the stack
            ans.append(count)  # Store how many people the current person can see
        return ans[::-1]  # Reverse the answer to maintain the original order