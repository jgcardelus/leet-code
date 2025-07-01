def findNearest(stockData, query):
    index = query - 1
    current_price = stockData[index]

    min_distance = len(stockData) + 1
    solution = -1

    for left in range(index, -1, -1):
        if stockData[left] < current_price:
            distance = index - left
            if distance < min_distance:
                solution = left
                min_distance = distance
                break

    for right in range(index, len(stockData)):
        if stockData[right] < current_price:
            distance = right - index
            if distance < min_distance:
                solution = right
                min_distance = distance
            break

    return solution + 1 if solution != -1 else -1

stockData = [5,6,8,4,9,10,8,3,6,4]
queries = [6,5,4]
solutions = []

for query in queries:
    solutions.append(findNearest(stockData, query))

print(solutions)
