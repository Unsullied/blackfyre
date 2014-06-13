from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.6)
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(250,250)
glutInitWindowPosition(0,0)
glutCreateWindow("Teapot")
glutDisplayFunc(draw)
glutMainLoop()
