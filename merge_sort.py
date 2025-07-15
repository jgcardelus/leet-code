def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    for x in range(i, len(left)):
        merged.append(left[x])

    for y in range(j, len(right)):
        merged.append(right[y])

    return merged

print(merge_sort([4,3,2,1]))
