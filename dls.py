graph= {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [], 
    'G': []
}
visited=[]

def dls(graph, start, goal, limit):
    stack=[(start, 0, [start])]
    visited=set([start])

    while stack:
        node,depth,path=stack.pop()
        if node==goal:
            return path
        if depth<limit:
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, depth+1, path+[neighbor]))

    return None

print(dls(graph,'A','G',3))
