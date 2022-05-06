from utilities.Window import Window

from utilities.TurtMath import atan2, tan, sin, cos, sign

class Turtle:
    def __init__(self, screenSize: list[int] = [400, 500], backgroundColor: tuple[float] = (0, 0, 0), animation: bool = False, turtleName: str = "Turtle") -> None:
        """
        Creates a window to show the plane in which the turtle can move.

        :param shape: the size of the window in pixels
        :param backgroundColor: the RGB-Values of the background from the plane in range of 0 to 1
        :param animation: if true you can see the turtle move, otherwise it only shows the result if asked
        :param turtleName: the name of the turtle
        :return: nothing
        """
        
        self.__screenSize = screenSize
        self.__screen = Window(self.__screenSize, backgroundColor, animation, turtleName)

        self.__position = (0, 0)
        self.__heading = 0

        self.__turtleColor = (1, 1, 1)
        self.__backgroundColor = backgroundColor
    
    # GetFunctions
    def getScreenSize(self) -> list[int]:
        """
        :return: size of the turtleplane
        """
        return self.__screenSize

    def getPos(self) -> tuple[float]:
        """
        :return: position of the turtle
        """
        return tuple(self.__position)

    def getHeading(self) -> float:
        """
        :return: heading of the turtle
        """
        return self.__heading

    def getTurtleColor(self) -> tuple[float]:
        """
        :return: a tuple with the RGB-Values of the turtle in range of 0 to 1
        """
        return self.__turtleColor

    # SetFunctions
    def setHeading(self, newHeading: float) -> None:
        """
        Set the heading of the turtle

        :param newHeading: the Value in degrees
        :return: nothing
        """
        self.__heading = newHeading - newHeading//360 * 360 - (newHeading - newHeading//360 * 360)//180 * 360

    def setPos(self, newPosition: tuple[float]) -> None:
        """
        Give the turtle a new position on the plane

        :param newPostion: the Coordinates of the new postion
        :return: nothing
        """
        self.__position = tuple(newPosition)

    def setTurtleColor(self, rgbValues: tuple[float]) -> None:
        """
        Set the color of the turtle

        :param rgbValues: tuple of RGB-Values in range 0 to 1
        :return: nothing
        """
        self.__screen.setTurtleColor(rgbValues)
        self.__turtleColor = rgbValues

    def setSpeed(self, speed: int) -> None:
        """
        Set the speed of the turtle

        :param speed: integer of the speed
        :return: nothing
        """
        self.__screen.setSpeed(speed)

    # RestFunctions
    def forward(self, distance: float) -> None:
        """
        Draw a line in direction of the heading of the turtle

        :param distance: the length of the line
        :return: nothing
        """
        if round(distance) == 0: pass

        else:
            m = round(tan(self.__heading - 90), 5)
            q = self.__position[1] - m*self.__position[0]

            if abs(m) >= 1 or abs(self.__heading) in [0, 180]:
                direction = int((2*(abs(self.__heading) < 90) - 1))
                destination = self.__position[1] + abs(cos(self.__heading)) * distance * direction

                for y in range(round(self.__position[1]), round(destination), sign(destination - self.__position[1])):
                    x = round((y - q)/m)

                    if (-self.__screenSize[1]/2 < round(x) < self.__screenSize[1]/2) and (-self.__screenSize[0]/2 < round(y) < self.__screenSize[0]/2): self.__screen.changePixel(self.__coordinateToPositionOnWindow([x, y]))

                x = (destination - q)/m
                if (-self.__screenSize[1]/2 < round(x) < self.__screenSize[1]/2) and (-self.__screenSize[0]/2 < round(destination) < self.__screenSize[0]/2): self.__screen.changePixel(self.__coordinateToPositionOnWindow([x, destination]))
                
                self.setPos(((destination - q)/m, destination))
            
            else:
                direction = -sign(self.__heading)
                destination = self.__position[0] + abs(sin(self.__heading)) * distance * direction

                for x in range(round(self.__position[0]), round(destination), sign(destination - self.__position[0])):
                    y = round(m*x + q)
                    
                    if (-self.__screenSize[1]/2 < round(x) < self.__screenSize[1]/2) and (-self.__screenSize[0]/2 < round(y) < self.__screenSize[0]/2): self.__screen.changePixel(self.__coordinateToPositionOnWindow([x, y]))

                y = m*destination + q
                if (-self.__screenSize[1]/2 < round(destination) < self.__screenSize[1]/2) and (-self.__screenSize[0]/2 < round(y) < self.__screenSize[0]/2): self.__screen.changePixel(self.__coordinateToPositionOnWindow([destination, y]))
                
                self.setPos((destination, y))

    def backward(self, distance: float) -> None:
        """
        Draw a line in opposite direction of the heading

        :param distance: length of the line
        :return: nothing
        """
        self.forward(-distance)

    def back(self, distance: float) -> None:
        """
        Draw a line in opposite direction of the heading

        :param distance: length of the line
        :return: nothing
        """
        self.forward(-distance)

    def goto(self, position: tuple[float]) -> None:
        """
        Draw a line to the given position from the turtles position. The heading will stay the same

        :param position: the coordinates to goto
        :return: nothing
        """
        if position != self.__position:
            heading = self.__heading
            
            x = position[0] - self.__position[0]
            y = position[1] - self.__position[1]
            r = (x**2 + y**2)**0.5
            
            self.setHeading(atan2(x, y) - 90)
                
            self.forward(r)
            
            self.__heading = heading

    def left(self, angle: float) -> None:
        """
        Turns the turtle by the given Value counterclockwise

        :param angle: angle to turn in degrees
        :return: nothing
        """
        self.setHeading(self.__heading + angle) 
    
    def right(self, angle: float) -> None:
        """
        Turns the turtle by the given Value clockwise

        :param angle: angle to turn in degrees
        :return: nothing
        """ 
        self.setHeading(self.__heading - angle)

    def penUp(self) -> None:
        """
        The turtle stops to draw when it moves

        :return: nothing
        """
        self.__screen.setTurtleColor(self.__backgroundColor)

    def penDown(self) -> None:
        """
        The turtle draws again

        :return: nothing
        """
        self.__screen.setTurtleColor(self.__turtleColor)

    def clear(self) -> None:
        """
        Clears the plane from all drawing

        :return: nothing
        """
        self.__screen.resetWindow()

    def showResult(self) -> None:
        """
        Shows the result of the drawings

        :return: nothing
        """
        self.__screen.show(0)

    def circle(self, radius: float, degrees: float = 360) -> None:
        """
        Draws an circle. If the radius is negative, the center of the circle is 90° to the left from the turtle heading, otherwise to the right. 
        When degrees is positive, the turtle will move forward, otherwise backwards.

        :param radius: the radius in pixel
        :param degrees: the arc in degrees
        :return: nothing
        """
        if abs(self.__heading) < 90: m = [self.__position[0] + radius*cos(self.__heading), self.__position[1] + radius*sin(self.__heading)]
        else: m = [self.__position[0] - radius*cos(180 - abs(self.__heading)), self.__position[1] + radius*sin(sign(self.__heading)*abs((180 - abs(self.__heading))))]
        
        correctionOfRadius = -sign(radius)
        for d in range(correctionOfRadius*int((self.__heading - 2*self.__heading+180)), correctionOfRadius*(int((self.__heading + degrees - 2*self.__heading+180)) + 1*sign(degrees)), correctionOfRadius*sign(degrees)): #here is the problem
            pos = [int(m[0] + cos(d)*radius), int(m[1] + sin(d)*radius)]
            self.goto(pos)

        self.setPos(pos)
        self.setHeading(self.__heading - degrees)

    # PrivateFunctions
    def __coordinateToPositionOnWindow(self, positionTurtle: list[int]) -> tuple:
        """
        Calculate the position in the numpy-Array from a given position of the turtle

        :param positionTurtle: list of the postion from the turtle
        :return: tuple with the position in the numpy Array
        """
        return tuple([round(positionTurtle[0] + self.__screenSize[1]/2), round(-positionTurtle[1] + self.__screenSize[0]/2)]) 