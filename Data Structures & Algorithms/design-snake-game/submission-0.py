class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.x = width
        self.y = height
        self.pos = deque([[0,0]])
        self.food = list(reversed(food))
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        newPos = [self.pos[0][0] + self.movement[direction][0],
            self.pos[0][1] + self.movement[direction][1]]
        
        if (
            newPos[0] not in range(self.y) or newPos[1] not in range(self.x) or
            any(newPos == p for p in self.pos)
            ):
            return -1
        if self.food and newPos == self.food[-1]:
            self.food.pop()
        else:
            self.pos.pop()
        self.pos.appendleft(newPos)

        return len(self.pos) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
