class Solution:
    def maxDistance(self, moves: str) -> int:
        pos = [0, 0]
        _ = 0
        for move in moves:
            if move == "U":
                pos[1] += 1
            elif move == "D":
                pos[1] -= 1
            elif move == "R":
                pos[0] += 1
            elif move == "L":
                pos[0] -= 1
            else:
                _ += 1
        if pos[0] >= 0:
            pos[0] += _
        else:
            pos[0] -= _
        return abs(pos[0]) + abs(pos[1])