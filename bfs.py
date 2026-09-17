from collections import deque 

graph= {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [], 
    'G': []
}

def bfs(graph, start, goal):
    queue= deque([start])
    visited= set([start])
    parent={start: None}

    while queue:
        node= queue.popleft()
        if node == goal:
            path=[]
            while node is not None:
                path.append(node)
                node= parent[node]
            return path[::-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=node
                queue.append(neighbor)

    return None

print(bfs(graph, 'A', 'E'))