# PyFunc.py
# Plotting functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
def my_range(start,end,step):
    x=start
    l=[]
    while (x<end):
        l.append(x)
        x+=step
    return l

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-2.0, 2.0, -4.0, 4.0)
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(4.0)
    glBegin(GL_LINE_STRIP)
    for x in my_range(-2.0, 2.0, 0.1):
        y = log(x)
        glVertex2f(x, y)
        if y==-1 or y==1:
            glEnd()
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
            glBegin(GL_LINE_STRIP)
    glEnd()
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINE_STRIP)
    for x in my_range(-360.0,360.0,0.1):
        y=cos(radians(x))
        glVertex2f(x,y)
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(-360.0, 0.0)
    glVertex2f(360.0, 0.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, -2.0)
    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowPosition(50,50)
glutInitWindowSize(400,400)
glutCreateWindow("Function Plotter")
glutDisplayFunc(plotfunc)
init()
glutMainLoop()
