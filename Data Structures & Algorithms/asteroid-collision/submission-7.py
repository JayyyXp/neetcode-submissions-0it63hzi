class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        helper = list(asteroids)

        while True:
            temp = [helper[0]]
            i = 1
            while i < len(helper):
                print(helper[i])
                if len(temp) == 0:
                    temp.append(helper[i])
                elif temp[-1] > 0 and helper[i] > 0:
                    temp.append(helper[i])
                elif temp[-1] < 0 and helper[i] < 0:
                    temp.append(helper[i])
                elif temp[-1] < 0 and helper[i] > 0:
                    temp.append(helper[i])
                elif -temp[-1] == helper[i]:
                    temp.pop()
                elif abs(temp[-1]) > abs(helper[i]):
                    pass
                elif abs(temp[-1]) < abs(helper[i]):
                    temp.pop()
                    temp.append(helper[i])
                i += 1
            if (len(temp) == len(helper)):
                return helper
            elif len(temp) == 0:
                return [] 
            else:
                helper = list(temp)


