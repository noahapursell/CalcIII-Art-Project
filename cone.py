from ellipse import Ellipse
import vpython as vp 
from colors import Colors
import random


class Cone:
    """A class to represent a "cone" that extends from one leaf to another leaf"""

    def __init__(self, top_ellipse: Ellipse, y_value:float = 0, scaling_factor:float = 1, height: float = 7, parent_leaf_height = 0.1):
        """Create a cone stemming from the top_ellipse and going down to a point, with a copy of top_ellipse scaled by scaling_factor
        at its bottom"""
        self.y = y_value
        self.height = height
        self.parent_leaf_height = parent_leaf_height
        self.scaling_factor = scaling_factor
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
    
    def set_opacity(self, opacity: float):
        """Set the opacity (see-though ness) of the object
        0 = transparent, 1 = no transparency"""

        self.__cone.opacity = opacity

    def get_leaf(self, height: float = None,  num_holes: float = None):
        from leaf import Leaf

        """Return a leaf object that is a reduced size of the parent leaf object"""
        if num_holes is None:
            num_holes = random.uniform(1, 15)
        if height is None:
            height = self.parent_leaf_height * self.scaling_factor
        l = Leaf(self.__bottom_ellipse, height = height, y = self.y - self.height)
        l.set_visibility(True)
        l.set_opacity(0.6)

        return l
        



    