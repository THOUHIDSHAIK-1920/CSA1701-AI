a = int(input("Enter capacity of jug A: "))
b = int(input("Enter capacity of jug B: "))
goal = int(input("Enter goal amount: "))

x = 0
y = 0

while x != goal and y != goal:
    if x == 0:
        x = a
    elif y == b:
        y = 0
    else:
        t = min(x, b - y)
        x = x - t
        y = y + t

    print("A =", x, "B =", y)

print("Goal reached")
