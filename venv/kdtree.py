from point_generator import random_square, circle

N_POINTS = 5

sq = random_square(N_POINTS)
print(sq)

def kd_tree(points,axis):
    # axis = "x" or "y"
    # if len(points) == 1, only print point and return
    if len(points) == 1:
        print(points)
        return points
    # sort points according to axis
    # sort according to x
    left = 0
    right = len(points)
    mid = (left+right)//2
    if axis == "x":
        points.sort(key = lambda p: p[0])  # x axis
    elif axis == "y":
        points.sort(key = lambda p: p[1])  # y axis
    left_part = points[:mid]
    right_part = points[mid:]
    middle_point = left_part [-1]
    print("Axis {}: {}, before: {}, after: {}". format(axis,middle_point, left_part, right_part))

    if axis =="x":
        kd_tree(left_part,"y")
        kd_tree(right_part,"y")
    elif axis == "y":
        kd_tree(left_part,"x")
        kd_tree(right_part,"y")

    # find coordinate of the middle point
    # split points to two halves
    # print each half
    # recurse o each half

kd_tree(sq,"x")