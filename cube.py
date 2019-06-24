import numpy as np
import copy

class cube:
    def __init__(self, dim):
        self.s = dim
        self.faces = []
        self.swaps = [[1, 2, 3, 4], [0, 4, 5, 2], [0, 1, 5, 3], [0, 2, 5, 4], [0, 3, 5, 1], [1, 4, 3, 2]]

        for i in range(6):
            self.faces.append(face(dim, i)) # 0 = white, 1 = green, 2 = red, 3 = blue, 4 = orange, 5 = yellow

        self.faces = np.asarray(self.faces)

    def turn(self, f, depth, direction):
        cpy = copy.deepcopy(self.faces)

        if depth <= self.s / 2 and depth > 0:
            for i in range(self.s):
                for j in range(self.s):
                    self.faces[f].arr[i, j] = cpy[f].arr[j, self.s - i - 1] if direction == 1 else cpy[f].arr[self.s - j - 1, i] # turns the face, itself (effect of depth = 0)
            for i in range(4):
                if f == 0:
                    print(i)
                    if direction == 1:
                        self.faces[self.swaps[f][i]].arr[:, :depth] = cpy[self.swaps[f][i+1 if i+1 < 4 else 0]].arr[:, :depth]
                    else:
                        self.faces[self.swaps[f][3-i]].arr[:, :depth] = cpy[self.swaps[f][3-i-1 if 3-i-1 >= 0 else 3]].arr[:, :depth]
                elif f == 1:
                    pass

    def __str__(self):
        val = ''

        for f in self.faces:
            for i in range(self.s):
                for j in range(self.s):
                    # print(f.arr[i, j].color)
                    val = val + str(f.arr[i, j].color)

        return val

class face:
    def __init__(self, dim, color):
        self.arr = []
        self.s = dim
        for i in range(self.s):
            self.arr.append([])

        for i in range(self.s):
            for j in range(self.s):
                self.arr[i].append(cubie(color))

        self.arr = np.asarray(self.arr)

class cubie:
    def __init__(self, c):
        self.color = c

if __name__ == '__main__':
    c = cube(3)
    print(c)
    c.turn(0, 1, 1)
    print(c)
    c.turn(0, 1, -1)
    print(c)
