# 1 2 1 3 4 6
#   x i j
#       x < j -> j
#       x > j -> x
#       x == j -> edges

def find_peak(array):
    def do_find_peak(array, left, right):
        middle = (right - left) // 2 + left

        left_neighbor = array[middle] - 1
        if middle - 1 >= 0:
            left_neighbor = array[middle - 1]

        right_neighor = array[middle] - 1
        if middle + 1 < len(array):
            right_neighor = array[middle + 1]

        # Peak
        if array[middle] > left_neighbor and array[middle] > right_neighor:
            return middle

        # find direction of next search
        if right_neighor > left_neighbor:
            return do_find_peak(array, middle + 1, right)
        else:
            return do_find_peak(array, left, middle-1)

    return do_find_peak(array, 0, len(array) - 1)

print(find_peak([1,2,3,1]))
print(find_peak([1,2,1,3,5,6,4]))
