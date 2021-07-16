import numpy as np

from PIL import Image

HEIGHT = 1024
WIDTH = 1024

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros((1024,1024,3), dtype=np.uint8)

def create_line(m: int, b: int):
    def line(x: int) -> int:
        return m*x + b

    return line

def alg_1():
    data = np.zeros((1024,1024,3), dtype=np.uint8)
    line = create_line(0.3, 0)

    for x in range(0, data.shape[1]):
        y = round(line(x))
        if y >= data.shape[0]: continue
        data[y, x] = [255, 0, 0]

    img = Image.fromarray(data)
    img.save("temp1.png")

def alg_2():
    data = np.zeros((1024,1024,3), dtype=np.uint8)
    m = 0.3
    b = 0
    line = create_line(m, b)

    y = line(0)
    y_rounded = round(y)
    data[y_rounded, 0] = [255, 0, 0]

    for x in range(1, data.shape[1]):
        y = y + m
        y_rounded = round(y)
        if y_rounded >= data.shape[0]: continue
        data[y_rounded, x] = [255, 0, 0]

    img = Image.fromarray(data)
    img.save("temp2.png")

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("alg_1()", globals=locals(), number=1))
    print(timeit.timeit("alg_2()", globals=locals(), number=1))