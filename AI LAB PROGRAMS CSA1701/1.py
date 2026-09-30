from collections import deque

def solve(start, goal):
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:
            print("Solution:", path + [state])
            return

        z = state.index(0)
        r, c = divmod(z, 3)

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                new = tuple(new)

                if new not in visited:
                    visited.add(new)
                    q.append((new, path))

start = tuple(map(int, input("Enter initial state: ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))

solve(start, goal)
