from collections import defaultdict

def check_bipartite(graph, node, color, c, visited):
    visited.add(node)
    color[node] = c
    for child in graph[node]:
        if child not in visited:
            temp = check_bipartite(graph, child, color, c^1, visited)
            if not temp:
                return False
        else:
            if color[child] == color[node]:
                return False
    return True


ipt = [[1,2],[2,3],[3,6],[6,5],[5,4],[1,4]]

graph = defaultdict(list)
visited = set()
color = {}

for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

print(check_bipartite(graph, 1, color, 0, visited))