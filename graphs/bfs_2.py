from collections import deque

def dfs(index, n, adj):
    q = deque()

    visited = [False] * n

    q.append(index)

    while q:
        node = q.popleft()
        print(node)
        visited[node] = True
        for connection in adj[node]:
            if not visited[connection]:
                q.append(connection)
    

def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)

if __name__ == "__main__":
    # Define graph
    n = 5
    i = 0
    adj = [[] for _ in range(n)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 2, 4)
    add_edge(adj, 1, 3)
    add_edge(adj, 4, 4)
    dfs(i, n, adj)
    