# should use the rest of sub array
#  is the subarray i times the rest or is it just i
# opt_i = max(i * opt(i+1), opt(i+1))
#
# Start at 0
#   max_product = max(i * opt(i+1), opt(i+1))
#
#

def max_subarray(array):
    max_integer = array[0]
    current_count = array[0]

    left, right = 0, 1

    while right < len(array):
        current_count *= array[right]

        if current_count >= max_integer:
            right += 1
            max_integer = current_count
        else:
            current_count /= array[left]
            left +=1

        if right == len(array):
            left += 1
            right = len(array) - 1

        if right == left:
            right += 1

    return max_integer

print(max_subarray([2,3,-2,4]))
