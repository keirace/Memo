from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs(graph, start):
    stack = [start]
    visited = set([start])
    result = []
    while stack:
        node = stack.pop()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return result

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    return result


# Example usage

# graph = {
#     0: [1, 2],
#     1: [0, 3, 4],
#     2: [0, 4],
#     3: [1],
#     4: [1, 2]
# }

# print("BFS:", bfs(graph, 0))
# print("DFS:", dfs(graph, 0))
# print("DFS (Recursive):", dfs_recursive(graph, 0))


def connectedComponent(isConnected):
    n = len(isConnected)
    visited = [False]*n
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if isConnected[i][j] and not visited[j]:
                dfs(j)

    groups = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            groups += 1
    return groups


################################################################
# Disjoint Set Union (DSU) or Union-Find to find connected components in a graph
# Time complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space complexity: O(V) for the parent array
################################################################

# Function to find the root parent of a node with path compression
def findParent(parent, x):
    if parent[x] == x:
        return x
        
    # Path compression
    parent[x] = findParent(parent, parent[x])  
    return parent[x]

# Function to unite two subsets
def unionSets(parent, x, y):
    px = findParent(parent, x)
    py = findParent(parent, y)
    print(f"Union: {x} and {y}, with parents {px} and {py}")
    if px != py:
        # Union operation
        parent[px] = py

def getComponents(V, edges):
    # Initialize each node as its own parent
    parent = [i for i in range(V)]
    print(f"Initial parent array: {parent}")

    # Union sets using the edge list
    for edge in edges:
        print(f"Processing edge: {edge}")
        unionSets(parent, edge[0], edge[1])

    print(f"Parent array after union operations: {parent}")
    # Apply path compression for all nodes
    for i in range(V):
        parent[i] = findParent(parent, i)

    # Group nodes by their root parent
    resMap = {}
    for i in range(V):
        root = parent[i]
        if root not in resMap:
            resMap[root] = []
        resMap[root].append(i)

    # Collect all components into a result list
    res = list(resMap.values())

    return res

V = 5

# Edge list as 2D array (list of lists)
edges = [
    [0, 1],
    [1, 2],
    [3, 4]
]

# Find connected components using DSU
res = getComponents(V, edges)

# Print connected components
for comp in res:
    print(" ".join(map(str, comp)))