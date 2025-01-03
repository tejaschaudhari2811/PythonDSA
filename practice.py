from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap = {}
        for time in times:
            hashmap[(time[0], time[1])] = time[2]
    
        connected_nodes = {node:[] for node in range(1, n+1)}
        for time in times:
            connected_nodes[time[0]].append(time[1])
        
        visited_nodes = set()

        def dfs(node, distance):
            if node in visited_nodes:
                return 0
            visited_nodes.add(node)
            min_distance = distance
            for current in connected_nodes[node]:
                min_distance = max(min_distance, dfs(current, distance+hashmap[(node, current)]))
            return min_distance

        distance = dfs(k,0)
        return dfs(k,0) if len(visited_nodes) == n else -1
        



        

            

# Example usage
c = Solution()
times=[[1,2,1],[2,3,1],[1,4,4],[3,4,1]]

c.networkDelayTime(times, 4, 1)
