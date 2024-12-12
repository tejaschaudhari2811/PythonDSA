from collections import deque

def bfs(adj, visited, starting_node):
    visited[starting_node] = True
    q = deque()
    q.append(starting_node)

    while q:
        current = q.popleft()
        print(current)
        for node in adj[current]:
            if not visited[node]:
                visited[node] = True
                q.append(node)  

def add_edge(adj, start, end):
    adj[start].append(end)
    adj[end].append(start)

if __name__ == "__main__":
    size = 5
    adj = [[] for _ in range(size)]
    edges = [[0,1], [0,3], [1,2], [2,4]]
    for e  in edges:
        add_edge(adj, e[0], e[1])
    visited = [False] * size
    bfs(adj, visited, 0)
