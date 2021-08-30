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

def aoc2015_2():
    def single_present(dimensions):
        print (dimensions)
        l, w, h = map(int, dimensions.split('x'))
        area_sides = (l*w, w*h, h*l)
        perimeter_sides = (l+w, w+h, h+l)
        smallest_perimeter = 2*min(perimeter_sides)
        volume = l*w*h
        ribbon = smallest_perimeter + volume
        smallest_side = min(area_sides)
        surface_area = 2*sum(area_sides) + smallest_side
        print(surface_area, ribbon)
        return surface_area, ribbon
    assert(single_present("2x3x4")== (58, 34))
    assert(single_present("1x1x10") == (43,14))
    input = open("2015/02/input")
    total_surface_area = 0
    total_ribbon = 0
    for present in input:
        surface_area, ribbon = single_present(present)
        total_surface_area += surface_area
        total_ribbon += ribbon
    return total_surface_area, total_ribbon
