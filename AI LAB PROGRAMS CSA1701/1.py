puzzle = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print("Initial State:")
print(puzzle[:3])
print(puzzle[3:6])
print(puzzle[6:])
puzzle[puzzle.index(0)], puzzle[7] = puzzle[7], puzzle[puzzle.index(0)]
print("Goal State:")
print(puzzle[:3])
print(puzzle[3:6])
print(puzzle[6:])

if puzzle == goal:
    print("Goal Reached")
else:
    print("Not Reached")
