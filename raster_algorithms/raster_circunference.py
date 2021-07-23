from image import create_canvas
from collections import namedtuple
from raster_line import RED, Point
from PIL import Image

def alg_1(r: int, center: Point):
    new_d = 0
    data = create_canvas()
    y = center.y + r
    data[center.x, y] = RED

    for x in range(center.x, center.x + r):
        if new_d < 0:
            y -= 1
            new_d += 2*x + 3
        else:
            new_d += 2*x - 2*y  + 5

        data[x, y] = RED
        data[x, -y] = RED
        data[-x, -y] = RED
        data[-x, y] = RED
        data[y, x] = RED
        data[y, -x] = RED
        data[-y, x] = RED
        data[-y, -x] = RED

    img = Image.fromarray(data)
    img.save("circunference/temp3.png")

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("alg_1(128, Point(512, 512))", globals=locals(), number=1))
