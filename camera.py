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
        if key == 'w':
            self.__xRotation -= 1.0
        elif key == 's':
            self.__xRotation += 1.0
        elif key == 'a':
            self.__yRotation -= 1.0
        elif key == 'd':
            self.__yRotation += 1.0

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

