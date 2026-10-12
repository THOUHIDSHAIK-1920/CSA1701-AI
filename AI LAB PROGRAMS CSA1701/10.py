
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [(h[start], 0, start)]
visited = []

while open_list:
    open_list.sort()
    f, cost, node = open_list.pop(0)

    if node == goal:
        print("Goal reached:", node)
        print("Cost:", cost)
        break

    if node not in visited:
        visited.append(node)

        for next_node, distance in graph[node]:
            if next_node not in visited:
                new_cost = cost + distance
                open_list.append((new_cost + h[next_node], new_cost, next_node))
else:
    print("Goal not found")
