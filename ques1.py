from collections import deque

initial = tuple(['R', 'R', 'R', '_', 'L', 'L', 'L'])
goal = tuple(['L', 'L', 'L', '_', 'R', 'R', 'R'])

def get_moves(state):
    moves = []
    s = list(state)
    for i, c in enumerate(s):
        if c == 'R':
            if i + 1 < 7 and s[i + 1] == '_':
                t = s[:]
                t[i], t[i + 1] = t[i + 1], t[i]
                moves.append(tuple(t))
            if i + 2 < 7 and s[i + 1] == 'L' and s[i + 2] == '_':
                t = s[:]
                t[i], t[i + 2] = t[i + 2], t[i]
                moves.append(tuple(t))
        if c == 'L':
            if i - 1 >= 0 and s[i - 1] == '_':
                t = s[:]
                t[i], t[i - 1] = t[i - 1], t[i]
                moves.append(tuple(t))
            if i - 2 >= 0 and s[i - 1] == 'R' and s[i - 2] == '_':
                t = s[:]
                t[i], t[i - 2] = t[i - 2], t[i]
                moves.append(tuple(t))
    return moves

def bfs():
    queue = deque([(initial, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_moves(state):
            queue.append((next_state, path + [state]))
    return None

def dfs():
    stack = [(initial, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_moves(state):
            stack.append((next_state, path + [state]))
    return None

print("BFS Path:")
for step in bfs():
    print(step)

print("\nDFS Path:")
for step in dfs():
    print(step)
