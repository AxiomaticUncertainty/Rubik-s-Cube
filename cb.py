import numpy as np
import copy
# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from Open.GLU import *

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

            if f == 0:
                if direction == 1:
                    self.faces[1].arr[:, :depth] = cpy[2].arr[:, :depth]
                    self.faces[2].arr[:, :depth] = cpy[3].arr[:, :depth]
                    self.faces[3].arr[:, :depth] = cpy[4].arr[:, :depth]
                    self.faces[4].arr[:, :depth] = cpy[1].arr[:, :depth]
                else:
                    pass
                    # self.faces[1].arr[:, :depth] = cpy[4].arr[:, :depth]
                    # self.faces[2].arr[:, :depth] = cpy[1].arr[:, :depth]
                    # self.faces[3].arr[:, :depth] = cpy[2].arr[:, :depth]
                    # self.faces[4].arr[:, :depth] = cpy[3].arr[:, :depth]
            elif f == 1:
                if direction == 1:
                    self.faces[0].arr[:, -depth:] = np.rot90(cpy[4].arr[-depth:, :], 1)
                    self.faces[4].arr[-depth:, :] = np.rot90(cpy[5].arr[:, :depth], 1)
                    self.faces[5].arr[:, :depth] = np.rot90(cpy[2].arr[:depth, :], 1)
                    self.faces[2].arr[:depth, :] = np.rot90(cpy[0].arr[:, -depth:], 1)
                else:
                    pass
                    # self.faces[0].arr[:, -depth:] = np.rot90(cpy[2].arr[:depth, :], 1)
                    # self.faces[2].arr[-depth:, :] = np.rot90(cpy[5].arr[:, :depth], 3)
                    # self.faces[5].arr[:, :depth] = np.rot90(cpy[4].arr[-depth:, :], 3)
                    # self.faces[4].arr[-depth:, :] = np.rot90(cpy[0].arr[:, -depth:], 1)
            elif f == 2:
                self.faces[0].arr[-depth:, :] = cpy[1].arr[-depth:, :]
                self.faces[1].arr[-depth:, :] = cpy[5].arr[-depth:, :]
                self.faces[5].arr[-depth:, :] = np.rot90(cpy[3].arr[:depth, :], 2)
                self.faces[3].arr[:depth, :] = np.rot90(cpy[0].arr[-depth:, :], 2)
            elif f == 3:
                self.faces[0].arr[:, :depth] = np.rot90(cpy[2].arr[-depth:, :], 3)
                self.faces[2].arr[-depth:, :] = np.rot90(cpy[5].arr[:, -depth:], 3)
                self.faces[5].arr[:, -depth:] = np.rot90(cpy[4].arr[:depth, :], 3)
                self.faces[4].arr[:depth, :] = np.rot90(cpy[0].arr[:, :depth], 3)
            elif f == 4:
                self.faces[0].arr[:depth, :] = np.rot90(cpy[3].arr[-depth:, :], 2)
                self.faces[3].arr[-depth:, :] = np.rot90(cpy[5].arr[:depth, :], 2)
                self.faces[5].arr[:depth, :] = cpy[1].arr[:depth, :]
                self.faces[1].arr[:depth, :] = cpy[0].arr[:depth, :]
            elif f == 5:
                self.faces[1].arr[:, -depth:] = cpy[4].arr[:, -depth:]
                self.faces[4].arr[:, -depth:] = cpy[3].arr[:, -depth:]
                self.faces[3].arr[:, -depth:] = cpy[2].arr[:, -depth:]
                self.faces[2].arr[:, -depth:] = cpy[1].arr[:, -depth:]

    def codeToColor(self, code):
        if code == 0:
            return 'w'
        elif code == 1:
            return 'g'
        elif code == 2:
            return 'r'
        elif code == 3:
            return 'b'
        elif code == 4:
            return 'o'
        else:
            return 'y'

    def __str__(self):
        val = ''

        for f in self.faces:
            for i in range(self.s):
                for j in range(self.s):
                    # print(f.arr[i, j].color)
                    val = val + str(self.codeToColor(f.arr[j, i].color))
                val = val + '\n'

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
    for i in range(6):
        c.turn(4, 1, 1)
        c.turn(0, 1, 1)
        c.turn(4, 1, 1)
        c.turn(4, 1, 1)
        c.turn(4, 1, 1)
        c.turn(0, 1, 1)
        c.turn(0, 1, 1)
        c.turn(0, 1, 1)

    print(c)
