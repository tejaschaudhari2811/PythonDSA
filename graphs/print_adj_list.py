# Print adjacency list
if __name__ == "__main__":
    V = 3
    edges = [[0,1], [1,2], [2,0]]
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")