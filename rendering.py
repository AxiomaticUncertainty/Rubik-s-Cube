import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cb import *

width = 2
dim = 3
c = cube(dim)

face_vert = [(7, 2, 1, 5), (5, 7, 6, 4), (4, 5, 1, 0), (0, 1, 2, 3), (3, 2, 7, 6), (6, 3, 0, 4)]

vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))

edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))

colors = [(1, 1, 1), (0, 1, 0), (1, 0, 0), (0, 0, 1), (1, 0.6, 0), (1, 1, 0)]

def form():
    glBegin(GL_QUADS)
    i = 0
    for surface in face_vert:
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
        i = i + 1

    glEnd()

def draw_face(face_vertices, f, axis):


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0.0, 0.0, -10)

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        form()
        glRotatef(1, 1, 1, 1)
        pygame.display.flip()

main()
