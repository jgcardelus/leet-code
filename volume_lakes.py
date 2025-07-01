# Two pointers
# start and end of container
# while start > end:
#   record length
#   move end
#
# calculate volume min(height[start], height[end])
# move pointers to end, end+1
#
# repeat until reached end

def calculate_volume(heights):
    if len(heights) <= 2:
        return 0

    start, end = 0, 1

    volume = 0
    while end < len(heights):
        bowl = 0
        while end < len(heights) and heights[start] > heights[end] :
            bowl += heights[start] - heights[end]

        if end == len(heights):
            break

        volume += (end - start - 1) * min(heights[start], heights[end])
        start = end
        end += 1

    return volume

print(calculate_volume([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]))
print(calculate_volume([3,1,3]))
