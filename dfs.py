graph= {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [], 
    'G': []
}

def dfs(graph, start, goal):
    stack= [start]
    visited= set([start])
    parent={start: None}

    while stack:
        node= stack.pop()
        if node == goal:
            path=[]
            while node is not None:
                path.append(node)
                node=parent[node]
            return path[::-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=node
                stack.append(neighbor)
    return None

print(dfs(graph,'A','E'));