
class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if column < 0:
            raise ValueError("column not positive")
        if row >= 8:
            raise ValueError("row not on board")
        if column >= 8:
            raise ValueError("column not on board")
        else:
            self.location = (row, column)


    def can_attack(self, another_queen):
        if self.location == another_queen.location:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.location[0] < 0:
            raise ValueError("row not positive")
        if self.location[1] < 0:
            raise ValueError("column not positive")
        if self.location[0] >= 8:
            raise ValueError("row not on board")
        if self.location[1] >= 8:
            raise ValueError("column not on board")
        if self.location[0] == another_queen.location[0]:
            return True
        if self.location[1] == another_queen.location[1]:
            return True
        isdiagonal = False
        for i in range(8):
            if self.location[0] + i == another_queen.location[0] and self.location[1] + i == another_queen.location[1]:
                isdiagonal = True
                break
            if self.location[0] - i == another_queen.location[0] and self.location[1] - i == another_queen.location[1]:
                isdiagonal = True
                break
            if self.location[0] + i == another_queen.location[0] and self.location[1] - i == another_queen.location[1]:
                isdiagonal = True
                break
            if self.location[0] - i == another_queen.location[0] and self.location[1] + i == another_queen.location[1]:
                isdiagonal = True
                break
        return isdiagonal