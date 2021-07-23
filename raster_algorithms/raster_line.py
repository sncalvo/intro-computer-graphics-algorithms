import numpy as np

from collections import namedtuple
from PIL import Image

HEIGHT = 1024
WIDTH = 1024

RED = [255, 0, 0]

def create_canvas():
    return np.zeros((1024,1024,3), dtype=np.uint8)

def create_line(m: int, b: int):
    def line(x: int) -> int:
        return m*x + b

    return line

def alg_1():
    data = create_canvas()
    line = create_line(1.0, 0)

    for x in range(0, data.shape[1]):
        y = round(line(x))
        if y >= data.shape[0]: continue
        data[y, x] = RED

    img = Image.fromarray(data)
    img.save("line/temp1.png")

def alg_2():
    data = create_canvas()
    m = 1.0
    b = 0
    line = create_line(m, b)

    y = line(0)
    y_rounded = round(y)
    data[y_rounded, 0] = RED

    for x in range(1, data.shape[1]):
        y += m
        y_rounded = round(y)
        if y_rounded >= data.shape[0]: continue
        data[y_rounded, x] = RED

    img = Image.fromarray(data)
    img.save("line/temp2.png")

Point = namedtuple("Point", ["x", "y"])
def alg_3(start: Point, end: Point):
    data = create_canvas()
    data[start.x, start.y] = RED

    d_y = end.y - start.y
    d_x = end.x - start.x
    b, a = - d_x, d_y

    new_d = 2 * a + b
    y = start.y
    for x in range(start.x + 1, min(data.shape[1], end.x + 1)):
        if new_d > 0:
            y += 1
            new_d += (a + b)
        else:
            new_d += a

        data[x, y] = RED

    img = Image.fromarray(data)
    img.save("line/temp3.png")

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("alg_1()", globals=locals(), number=1))
    print(timeit.timeit("alg_2()", globals=locals(), number=1))
    print(timeit.timeit("alg_3(Point(0, 0), Point(1024, 1024))", globals=locals(), number=1))
