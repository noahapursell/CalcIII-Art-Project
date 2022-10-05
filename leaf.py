from ellipse import Ellipse
import vpython as vp
import random


class Leaf:
    """A class to manage a leaf in the animation"""

    def __init__(self, ellipse: Ellipse, height=0.1, num_holes=3):
        """Create a new instance of Leaf, with a specifice major-axis, minor-axis, height/thickness, and number of holes"""
        self.__ellipse = ellipse
        self.__height = height
        self.__holes = self.generate_holes(num_holes)

    def generate_holes(self, num_holes: int) -> list:
        """Return a list of "holes" where a hole is a circle shape of datatype vp.Shape"""
        holes = []

        max_x = self.__ellipse.horizontal_axis * 0.75
        max_y = self.__ellipse.vertical_axis * 0.75
        max_axis = max(self.__ellipse.horizontal_axis, self.__ellipse.vertical_axis) * 0.6
        min_axis = max(self.__ellipse.horizontal_axis, self.__ellipse.vertical_axis) * 0.3

        e = Ellipse(0, 0, 1, 1)
        holes.append(e)
        while True:
            x = random.uniform(-max_x, max_x)
            y = random.uniform(-max_y, max_y)
            ax1 = random.uniform(min_axis, max_axis)
            ax2 = random.uniform(min_axis, max_axis)
            new_e = Ellipse(x, y, ax1, ax2)

            if Ellipse.ellipse_intersecting_ellipse(e, new_e) or not Ellipse.ellipse_in_ellipse(new_e, self.__ellipse):
                print("BAD ELLIPSE")
                continue
            else:
                print("GOOD ELIPSE")
                holes.append(new_e)
                break
        
        return holes
            

    def display(self) -> None:
        """Display the leaf in a vpython window"""
        shapes = [vp.shapes.ellipse(width = self.__ellipse.horizontal_axis, height = self.__ellipse.vertical_axis)]
        for hole in self.__holes:
            shapes.append(vp.shapes.ellipse(
                width = hole.horizontal_axis, 
                height = hole.vertical_axis, 
                pos=(hole.x_pos, hole.y_pos)))

        d = vp.extrusion(
            path=[vp.vec(0, 0, 0), vp.vec(0, self.__height, 0)],
            shape=shapes
        )

    @property
    def holes(self) -> list:
        return self.__holes