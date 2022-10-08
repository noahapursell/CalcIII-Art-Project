from ellipse import Ellipse
import vpython as vp 
from colors import Colors


class Cone:
    """A class to represent a "cone" that extends from one leaf to another leaf"""

    def __init__(self, top_ellipse: Ellipse, y_value:float = 0, scaling_factor:float = 0.1, height: float = 15):
        """Create a cone stemming from the top_ellipse and going down to a point, with a copy of top_ellipse scaled by scaling_factor
        at its bottom"""
        self.__top_ellipse = top_ellipse
        self.__bottom_ellipse = Ellipse(
            top_ellipse.x_pos,
            top_ellipse.y_pos,
            top_ellipse.horizontal_axis * scaling_factor,
            top_ellipse.vertical_axis * scaling_factor
        )
        self.__cone = vp.cone(
            pos=vp.vec(top_ellipse.y_pos, y_value, -top_ellipse.x_pos),
            size=vp.vec(height, top_ellipse.vertical_axis * 2, 2 * top_ellipse.horizontal_axis),
            axis=vp.vec(0, -1, 0),
            color=Colors.get_random_color()
        )
        self.__cone.visible = False
    
    def set_visibility(self, visibility: bool):
        """Make the object visible or not"""
        self.__cone.visible = visibility



    