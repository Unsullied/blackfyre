from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1.0, 1.0)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(0.0,0.0)
    glColor3f(0.0,1.0,0.0)
    glVertex2f(1.0,-1.0)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(-1.0,-1.0)
    glVertex2f(-1.0,1.0)
    glVertex2f(0,2)
    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(500,500)
glutInitWindowPosition(50,50)
glutCreateWindow("Plot Points")
glutDisplayFunc(plotpoints)
init()
glutMainLoop()
