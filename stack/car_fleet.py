from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size_dict = defaultdict(int)
        # Incorrect solution, does not factor in the fact that cars slow down because of the 
        # cars ahead. 

        for pos, speed in zip(position, speed):
            steps = 0
            total_position = pos
            while total_position < target:
                steps +=1 
                total_position += speed
            size_dict[pos] = steps
        
        return len(set(size_dict.values()))