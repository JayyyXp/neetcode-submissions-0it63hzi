class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        helper = []
        for a in asteroids:
            if not helper:
                helper.append(a)
            else:
                add = True
                while helper and helper[-1] > 0 and a < 0:
                    if abs(helper[-1]) == abs(a):
                        helper.pop()
                        add = False
                        break
                    elif abs(helper[-1]) > abs(a):
                        add = False
                        break
                    elif abs(helper[-1]) < abs(a):
                        helper.pop()
                if add:
                    helper.append(a)
                        
        return helper

