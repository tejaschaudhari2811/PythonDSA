ipt = [(1,2),(2,3),(1,3),(4,5),(5,6),(4,6)]
# undirected graph
n = 6
# Create an adjacency list

graph = {node:[] for node in range(1,n+1)}
for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)

def get_number_of_nodes(graph, node, visited):
    visited.add(node)
    count = 0
    for child in graph[node]:
        if child not in visited:
            count += get_number_of_nodes(graph, child, visited)
    return count + 1

visited = set()
for node in range(1, n+1):
    print(get_number_of_nodes(graph, node, visited))