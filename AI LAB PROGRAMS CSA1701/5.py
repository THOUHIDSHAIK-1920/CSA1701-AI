m = int(input("Enter missionaries: "))
c = int(input("Enter cannibals: "))

print("Initial State:", m, c)

print("Move 1: 2 Cannibals")
c -= 2
print("State:", m, c)

print("Move 2: 2 Missionaries")
m -= 2
print("State:", m, c)

print("Move 3: 1 Missionary and 1 Cannibal")
m += 1
c += 1
print("State:", m, c)

print("Goal Reached")
