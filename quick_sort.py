def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = len(numbers) // 2

    left = []
    right = []

    for i in range(len(numbers)):
        if i == pivot:
            continue

        if numbers[i] < numbers[pivot]:
            left.append(numbers[i])
        else:
            right.append(numbers[i])

    left = quick_sort(left)
    right = quick_sort(right)

    left.append(numbers[pivot])
    left.extend(right)

    return left

print(quick_sort([4,3,2,1]))
