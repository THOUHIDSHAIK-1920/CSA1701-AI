
colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

color = {}

for node in graph:
    for c in colors:
        if all(color.get(neighbor) != c for neighbor in graph[node]):
            color[node] = c
            break

print(color)
