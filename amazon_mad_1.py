# Given a list of pairs of flight codes, with a start and destination airport
# Build a function that returns a pair consisting on the start and final destination
#
# For example  [ ["CAI","MAD"],["MAD","FRA"],["FRA","SEA"] ] returns ["CAI","SEA"]

## CAI -> MAD -> FRA -> SEA
## CAI
## { cai: ["mad"]
##    mad: [],
##    sea: []


## (a,b) a comes from, b is goes to
## { car: (0, 1), mad: (1, 1), sea: (1, 0)


## Plant
## 1. intialize dict
## 2. iterate, update vlaues
## 3. search for the solution

# n -> cities

def find_flight_route(connections):
    ## { cai: (0, 1), mad: (1, 1), fra: (1, 1), sea: (1, 0) }
    direction = {}

    # O(n) m < n
    for start, end in connections:
        if start in direction:
            direction[start] = (direction[start][0], 1 + direction[start][1])
        else:
            direction[start] = (0, 1)

        if end in direction:
            direction[end] = (1 + direction[end][1], direction[end][1])
        else:
            direciton[end] = (1, 0)


    flight_start, flight_dest = None, None

    # O(n)
    for city in directions.keys():
        comes_from, goes_to = directions[city]
        if comes_from == 1 and goes_to == 1:
            continue

        if comes_from == 0:
            flight_start = city
        else:
            flight_end = city

    return (flight_start, flight_end)


# {["CAI","MAD"],["MAD","FRA"],["FRA", "CAI"],["CAI","FRA"],["FRA","SEA"]}
# CAI -> MAD -> FRA -> CAI -> FRA -> SEA
# cai: (1, 1)
## { cai: (20, 19), mad: (1, 1), fra: (2, 2), sea: (1, 0) }
