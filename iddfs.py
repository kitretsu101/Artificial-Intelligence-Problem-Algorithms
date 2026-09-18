graph= {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [], 
    'G': []
}

def dls(graph, start, goal, limit):
    def iddls(node, goal, limit, path):
        if node==goal:
            return path
        if limit==0:
            return "cutoff"

        cutoff_occured=False

        for neighbor in graph[node]:
            if neighbor not in path:
                result= iddls(neighbor, goal, limit-1, path+[neighbor])
                if result=="cutoff":
                    cutoff_occured=True
                elif result is not None:
                    return result
        return "cutoff" if cutoff_occured else None

    return iddls(start, goal, limit, [start]) 

def iddfs(graph, start, goal, max_depth=10):
        for depth in range(max_depth+1):
            print(f"Searching with depth limit: {depth}")
            result=dls(graph, start, goal, depth)

            if result !="cutoff" and result is not None:
                return result
            
        return None

path= iddfs(graph,'A','G')
print=("Path: ", path)
