from image import create_canvas
from collections import namedtuple
from raster_line import RED, Point
from math import ceil, sqrt
from PIL import Image

def draw_symetric_point(center: Point, offset: Point, data):
    x, y = offset
    data[center.y - y, center.x + x] = RED
    data[center.y + y, center.x + x] = RED
    data[center.y + y, center.x - x] = RED
    data[center.y - y, center.x - x] = RED
    data[center.y - x, center.x + y] = RED
    data[center.y + x, center.x + y] = RED
    data[center.y - x, center.x - y] = RED
    data[center.y + x, center.x - y] = RED

def alg_1(r: int, center: Point):
    d = 5/4 - r
    h = d - 1/4
    data = create_canvas()
    y = r

    for x in range(0, ceil(r / sqrt(2))):
        draw_symetric_point(center, Point(x, y), data)
        # h < -1/4, but they are integers. So < 0 will suffice
        if h < 0:
            h += 2*x + 3
        else:
            y -= 1
            h += 2*x - 2*y + 5

    img = Image.fromarray(data)
    img.save("circunference/temp3.png")

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("alg_1(64, Point(128, 128))", globals=locals(), number=1))
