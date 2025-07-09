class Solution:
    def carFleet(self, target, position, speed):
        # Dict w/ position: speed
        # Until dict is empty
        # Move all to next position, in case of same position speed min
        # If any at position target, remove

        pos_speed = sorted([[p,s] for p, s in zip(position, speed)], reverse=True)
        fleets = []

        for pos, spd in pos_speed:
            time_to_target = (target - pos) / spd
            # If time to target is less or equal
            # it catches up
            # thus, if it's not, it will be a new fleet
            if not fleets or time_to_target > fleets[-1]:
                fleets.append(time_to_target)

        return len(fleets)


solver = Solution()
print(solver.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
