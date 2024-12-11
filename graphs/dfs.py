# Depth first search on graphs
def add_edge(adj, start, end):
    adj[start].append(end)
    adj[end].append(start)

def dfs_rec(adj, visited, s):
    visited[s] = True

    print("Visited node is ", s)

    for node in adj[s]:
        if not visited[node]:
            dfs_rec(adj, visited, node)

def dfs(adj, source):
    visited = [False] * len(adj)
    dfs_rec(adj, visited, source)
    
if __name__ == "__main__":
    V = 5

    # Create adjacency list for all vertices
    adj = [[] for _ in range(V)]

    edges = [[1,2], [1,0], [2,0], [2,3], [2,4]]

    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1

    dfs(adj, source)
