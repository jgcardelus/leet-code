#  ltr -> max at each point
#  rtl -> max at each point
#  at every position max(ltr, rtl)

def volumes(heights):
    left_fill = [0] * len(heights)
    right_fill = [0] * len(heights)

    left_max = heights[0]
    for i in range(len(heights)):
        if heights[i] < left_max:
           left_fill[i] = left_max - heights[i]
        else:
           left_max = heights[i]

    right_max = heights[-1]
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] < right_max:
            right_fill[i] = right_max - heights[i]
        else:
            right_max = heights[i]

    volume = 0
    for i in range(len(heights)):
        volume += min(left_fill[i], right_fill[i])

    return volume




print(volumes([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]))
print(volumes([2,1,2,1,2]))
