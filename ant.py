
class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 1  # 0: up, 1: right, 2: down, 3: left

    def move(self, grid):
        if grid[self.x][self.y] == 0:
            grid[self.x][self.y] = -1
            self.direction = (self.direction + 1) % 4
        else:
            grid[self.x][self.y] = 0
            self.direction = (self.direction - 1) % 4

        if self.direction == 0:
            self.y = (self.y - 1) % len(grid[0])
        elif self.direction == 1:
            self.x = (self.x + 1) % len(grid)
        elif self.direction == 2:
            self.y = (self.y + 1) % len(grid[0])
        elif self.direction == 3:
            self.x = (self.x - 1) % len(grid)








    