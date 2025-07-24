from collections import deque

times = {
    'A': 5,
    'B': 10,
    'G': 20,
    'D': 25
}

def successors(state):
    left, right, time, side = state
    result = []
    if side == 'left':
        group = left
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                t = max(times[a], times[b])
                new_left = list(left)
                new_left.remove(a)
                new_left.remove(b)
                new_right = right + [a, b]
                result.append(((tuple(sorted(new_left)), tuple(sorted(new_right)), time + t, 'right'), (a, b)))
    else:
        group = right
        for person in group:
            t = times[person]
            new_right = list(right)
            new_right.remove(person)
            new_left = left + [person]
            result.append(((tuple(sorted(new_left)), tuple(sorted(new_right)), time + t, 'left'), (person,)))
    return result

def is_goal(state):
    left, right, time, side = state
    return len(left) == 0 and time <= 60

def bfs():
    start = (('A', 'B', 'G', 'D'), (), 0, 'left')
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if is_goal(current):
            return path
        if current in visited:
            continue
        visited.add(current)
        for new_state, move in successors(current):
            queue.append((new_state, path + [move]))
    return None

def dfs():
    start = (('A', 'B', 'G', 'D'), (), 0, 'left')
    stack = [(start, [])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if is_goal(current):
            return path
        if current in visited:
            continue
        visited.add(current)
        for new_state, move in successors(current):
            stack.append((new_state, path + [move]))
    return None

print("BFS Solution:", bfs())
print("DFS Solution:", dfs())
