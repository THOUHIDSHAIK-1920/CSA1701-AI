
import itertools

n = int(input("Enter number of cities: "))
d = []

for i in range(n):
    d.append(list(map(int, input("Enter distances: ").split())))

p = list(range(1, n))
best = 9999

for path in itertools.permutations(p):
    cost = d[0][path[0]]

    for i in range(n - 2):
        cost += d[path[i]][path[i + 1]]

    cost += d[path[-1]][0]

    if cost < best:
        best = cost

print("Minimum distance:", best)
