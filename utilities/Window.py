import numpy as np
import cv2 as cv

class Window:
    def __init__(self, shape: list[int], backgroundColor: tuple[float] = (0, 0, 0), animation: bool = False, turtleName: str = "Turtle") -> None:
        """
        Creates a window to show the plane in which the turtle can move.

        :param shape: the size of the window in pixel
        :param backgroundColor: the RGB-Values of the background from the plane in range of 0 to 1
        :param animation: if true you can see how the turtle move, else it shows only the result if asked
        :param turtleName: the name of the turtle
        :return: nothing
        """
        
        self.__shape = shape
        self.__shape.append(3) # for the RGB values
        self.__windowPermanent = np.zeros(self.__shape)

        self.__backgroundColor = backgroundColor
        self.resetWindow()

        self.__animation = animation
        self.__windowName = turtleName

        self.__turtleColor = (1, 1, 1)
        self.__counterAnimation = 0
        self.__speed = 0
    
    def resetWindow(self) -> None:
        """
        Deletes all drawing on the plane

        :return: nothing
        """
        for firstLayer in self.__windowPermanent: 
            for secondLayer in firstLayer:
                for i in range(3):
                    secondLayer[i] = self.__backgroundColor[i]
        
    def setAnimation(self, animation: bool) -> None:
        """
        Set if the Turtle has to show the way he draws or not.
        
        :param animation: boolean of animation
        :return: nothing
        """ 
        self.__animation = animation
    
    def setSpeed(self, speed: int) -> None:
        """
        Set the speed which the Turtle use to draw, if the animation is activatet.

        :param speed: value of the speed
        :return nothing
        """
        if speed == -1: self.__animation = False
        else: self.__speed = speed
    
    def setTurtleColor(self, rgbValues: tuple[float]) -> None:
        """
        Set the color with them the Turtle draw.

        :param RGBValues: tuple with the RGB-Values in range of 0 to 1
        :return: nothing
        """
        self.__turtleColor = rgbValues 

    def getTurtleColor(self) -> tuple[float]:
        """
        :return: rgb-Values of the turtle in range of 0 to 1
        """
        return self.__turtleColor

    def changePixel(self, position: tuple[int]) -> None:
        """
        Colors a Pixel with the Color from the Turtle and show the change if the animation is activated

        :param position: tuple with the position of the pixel which have to change
        :return: nothing
        """
        self.__windowPermanent[position[1]][position[0]] = self.__turtleColor
        if self.__animation:
            if self.__counterAnimation > self.__speed: 
                self.show()
                self.__counterAnimation = 0
            else: self.__counterAnimation += 1
    
    def show(self, wait: int = 1) -> None:
        """
        Shows the plane with the draws

        :param wait: shows the Turtleplane this time in milliseconds, if wait = 0 it stay until you close it
        :return: nothing
        """
        cv.imshow(self.__windowName, self.__windowPermanent)
        cv.waitKey(wait)
