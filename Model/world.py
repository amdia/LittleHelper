#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The world module
    ===================

    Used to represent the world

"""

import threading
from car import Car
from path import Path

class World():
    """
        The world is composed of :
            >>> 1 car
            >>> 1 path
            >>> 1 current distance traveled
            >>> 1 real distance traveled
            >>> 1 boolean to reset the disatance
            >>> 1 boolean to confirm the reset
    """

    def __init__(self, car):
        self.car = car
        self.path = Path()

        # Distance management
        self.current_distance = 0
        self.real_distance = 0
        self.reset_distance = False
        self.ack_reset_distance = False

        # ==========================
        # Semaphore used in the code
        # ==========================

        # semaphore[1] shared with spi process
        self.sema_distance = threading.Semaphore()
        # semaphore[1] shared with video process
        self.sema_band_xcoord = threading.Semaphore()


    @property
    def car(self):
        """
            The object reprenting the car

            :getter: Returns the car
            :setter: Sets the car
            :type: Car
        """
        return self.car

    @property
    def path(self):
        """
            The object path representing current path

            :getter: Returns the path
            :setter: Sets the path
            :type: Path
        """
        return self.path

    @property
    def current_distance(self):
        """
            The current distance traveled by the car.
            This distance is calculated thanks to the odometry.

            :getter: Returns the distance
            :setter: Sets the distance
            :type: int
        """
        return self.current_distance

    @property
    def real_distance(self):
        """
            The real distance traveled by the car.
            This distance is the distance managed with the band.

            :getter: Returns the distance
            :setter: Sets the distance
            :type: int
        """
        return self.real_distance

    @property
    def reset_distance(self):
        """
            The boolean to ask the stm32 to reset the distance.

            :getter: Returns the reset_distance value
            :setter: Sets the reset_distance value
            :type: boolean
        """
        return self.reset_distance

    @property
    def ack_reset_distance(self):
        """
            The boolean to ack the reset distance from the stm32.

            :getter: Returns the ack_reset_distance value
            :setter: Sets the ack_reset_distance value
            :type: boolean
        """
        return self.ack_reset_distance

    def set_distance(self, distance1, distance2):
        """
            The distance save is the average from the distance of both wheels.

            :param distance1: The distance of the first wheel
            :type distance1: int
            :param distance2: The distance of the second wheel
            :type distance2: int

            :setter: Sets the current distance value
            :type: int
        """
        self.current_distance = (distance1 + distance2)/2
