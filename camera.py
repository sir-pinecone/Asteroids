from OpenGL.GL import *
from OpenGL.GLU import *

from vector3 import Vector3
import config


class Camera(object):
    """
    Simple OpenGL camera.
    """
    def __init__(self, origin=Vector3(0.0, 0.0, -90.0)):
        self.__xRotation = 0.0
        self.__yRotation = 0.0
        self.__position = origin

    def update(self, key):
        if key == 'a':
            self.__position[0] += 2.0 # move left
        elif key == 'd':
            self.__position[0] -= 2.0 # move right
        elif key == 'w':
            self.__position[1] -= 2.0 # move up
        elif key == 's':
            self.__position[1] += 2.0 # move down
        elif key == 'q':
            self.__position[2] += 2.0  
        elif key == 'e':
            self.__position[2] -= 2.0
        elif key == 'j':
            self.__yRotation += 2.0
        elif key == 'l':
            self.__yRotation -= 2.0
        elif key == 'i':
            self.__xRotation += 2.0
        elif key == 'k':
            self.__xRotation -= 2.0
        # add rotation

    def resize(self, width, height):
        if height == 0:
            height = 1

        # Reset the viewport and perspective transformation
        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = float(width)/float(height)

        gluPerspective(config.WINDOW_PERSPECTIVE, aspectRatio, config.NEAR, 
                       config.FAR)
        
        glMatrixMode(GL_MODELVIEW)

    def setup(self):
        # Clear the frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Reset the camera back to the origin
        glLoadIdentity()

        # TODO: Use gluLookAt instead?
        glTranslatef(self.__position[0], self.__position[1], 
                     self.__position[2])
        glRotatef(self.__xRotation, 1.0, 0.0, 0.0)
        glRotatef(self.__yRotation, 0.0, 1.0, 0.0)

