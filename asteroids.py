# -------------------------------------------------------------------------
# Asteroids v0.1
# Michael Campagnaro - 2010
# -------------------------------------------------------------------------

import OpenGL
OpenGL.ERROR_CHECKING = True # set to false for production
from OpenGL.GL import *
from OpenGL.GLUT import *
from time import time

from camera import Camera
from vector3 import Vector3
import config

# Create a camera 
camera = Camera(Vector3(0.0,0.0,-30.0)) 

# Track the running time
oldTime = time()
elapsedTime = 0.0

def initialize():
    glClearColor(0.0, 0.0, 0.0, 0.0) # black
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def resize(width, height):
    camera.resize(width, height)

def draw():
    global oldTime, elapsedTime
    
    currentTime = time()
    delta = currentTime - oldTime
    oldTime = currentTime

    # slow motion ratio can be used to slow things down!
    # delta /= config.slowMotionRatio
    elapsedTime += delta

    # Number of calculations to do on this frame
    numIterations = int(delta / config.maxDelta) + 1 

    if numIterations != 0:
        delta /= numIterations

    for i in xrange(numIterations):
        # update the simulation here
        pass

    camera.setup()

    # Draw a triangle for the hell of it
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()
    
    # Draw the frame
    glutSwapBuffers()

def keyboard(key, x, y):
    camera.update(key)

def main():
    # Initialize GLUT first
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_ALPHA)
    glutInitWindowSize(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    
    # Create the GLUT window
    window = glutCreateWindow(config.WINDOW_TITLE)
       
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutReshapeFunc(resize)
    glutKeyboardFunc(keyboard)

    # Run our own initialization
    initialize()

    # Start the event loop
    glutMainLoop()

# Start the game
main() 
