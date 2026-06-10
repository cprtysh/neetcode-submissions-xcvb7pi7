class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_indices=sorted(range(len(position)),key=lambda i:position[i])
        fleet_count,prev_time=0,0
        for index in sorted_indices[::-1]:
            time_to_target=(target-position[index])/speed[index]
            if time_to_target>prev_time:
                fleet_count+=1
                prev_time=time_to_target
        return fleet_count