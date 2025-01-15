def detect_cycle(graph, node, visited, par):
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            return detect_cycle(graph, child, visited, node)
        else:
            if child == par:
                return True
    return False