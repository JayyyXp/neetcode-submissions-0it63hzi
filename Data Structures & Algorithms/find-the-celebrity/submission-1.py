# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        personTo = defaultdict(list)
        toPerson = defaultdict(list)
        print(knows(1,1))
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i,j):
                    personTo[i].append(j)
                    toPerson[j].append(i)
        print(personTo, personTo[1])
        print(toPerson, toPerson[1])
        for i in range(n):  
            if len(personTo[i]) == 0 and len(toPerson[i]) == (n-1):
                return i
        return -1
