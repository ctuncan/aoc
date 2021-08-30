def aoc2015_1():
    input = open("2015/01/input").read()
    floor = 0
    first_basement = None
    for i, ch in enumerate(input):
        if ch == "(":
            floor += 1
        elif ch == ")":
            floor -= 1
        else:
            raise RuntimeError("Invalid Input")

        # Part 2: Which instruction first causes entry to the basement.
        # Note that the entries are 1 indexed, hence i+1
        if floor == -1 and first_basement is None:
            first_basement = i + 1
    return floor, first_basement
