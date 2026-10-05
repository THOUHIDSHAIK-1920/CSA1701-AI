puzzle = list(map(int, input("Enter puzzle: ").split()))
goal = list(map(int, input("Enter goal: ").split()))

print("Initial State:")
print(puzzle[:3])
print(puzzle[3:6])
print(puzzle[6:])

puzzle[puzzle.index(0)], puzzle[7] = puzzle[7], puzzle[puzzle.index(0)]

print("After Move:")
print(puzzle[:3])
print(puzzle[3:6])
print(puzzle[6:])

if puzzle == goal:
    print("Goal Reached")
else:
    print("Not Reached")
