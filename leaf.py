from ellipse import Ellipse
import vpython as vp
import random
import matplotlib.pyplot as plt
from colors import Colors
from cone import Cone


class Leaf:
    """A class to manage a leaf in the animation"""

    def __init__(self, ellipse: Ellipse, height=0.1, y: int = 0, num_holes: int = 5):
        """Create a new instance of Leaf, with a specifice major-axis, minor-axis, height/thickness, and number of holes"""
        self.__ellipse = ellipse
        self.__height = height
        self.__holes = self.get_holes(num_holes)
        self.y = y
        # self.plot()
        self.leaf = self.__get_leaf()

    def __get_leaf(self):
        """Display the leaf in a vpython window"""
        # shapes = [vp.shapes.ellipse(width=self.__ellipse.horizontal_axis, height=self.__ellipse.vertical_axis, pos=(
        #     self.__ellipse.x_pos, self.__ellipse.y_pos))]
        xs, ys = self.__ellipse.get_points()
        shapes = [[[x, ys[ind]] for ind, x in enumerate(xs)]]
        for hole in self.__holes:
            xs, ys = hole.get_points()
            shapes.append([[x, ys[ind]] for ind, x in enumerate(xs)])
        leaf = vp.extrusion(
            path=[vp.vec(0, 0, 0), vp.vec(0, self.__height, 0)],
            shape=shapes
        )

        leaf.pos.y = self.y

        leaf.color = Colors.get_random_color()
        leaf.visible = False

        return leaf

    def get_holes(self, num_holes) -> list:
        """Return a list of non-intersecting holes that are all inside the main ellipse, where the number of 
        holes is specified by num_holes"""
        holes = []

        for i in range(num_holes):
            # Initialize initial ranges
            needs_hole = True
            x_max = self.__ellipse.x_pos + self.__ellipse.horizontal_axis * 0.75
            x_min = self.__ellipse.x_pos - self.__ellipse.horizontal_axis * 0.75

            y_max = self.__ellipse.y_pos + self.__ellipse.vertical_axis * 0.75
            y_min = self.__ellipse.y_pos - self.__ellipse.vertical_axis * 0.75

            horizontal_ax_max = self.__ellipse.horizontal_axis * 0.5
            horizontal_ax_min = self.__ellipse.horizontal_axis * 0.1
            vertical_ax_max = self.__ellipse.vertical_axis * 0.5
            vertical_ax_min = self.__ellipse.vertical_axis * 0.1

            scaling_factor = 1.1

            while needs_hole:
                """Repeat forever until a valid ellipse is found"""
                scaling_factor -= 0.1
                x = random.uniform(x_min, x_max)
                y = random.uniform(y_min, y_max)
                v_ax = max(vertical_ax_min, random.uniform(
                    vertical_ax_min, vertical_ax_max * scaling_factor))
                h_ax = max(horizontal_ax_min, random.uniform(
                    horizontal_ax_min, horizontal_ax_max * scaling_factor))

                new_hole = Ellipse(x, y, h_ax, v_ax)

                if not Ellipse.ellipse_in_ellipse(new_hole, self.__ellipse):
                    # If the new hole is not inside the parent ellipse, make a new one
                    continue

                intersects_other_hole = False
                for hole in holes:
                    if Ellipse.ellipse_intersecting_ellipse(hole, new_hole):
                        intersects_other_hole = True
                        break
                    if Ellipse.ellipse_intersecting_ellipse(new_hole, hole):
                        intersects_other_hole = True
                        break
                if intersects_other_hole:
                    # If the new hole intersects with a previous hole, make a new one
                    continue

                # If the hole passes these two tests, add it to holes and make the next one
                holes.append(new_hole)
                needs_hole = False

        return holes

    def plot(self):
        shapes = [self.__ellipse] + self.holes

        for shape in shapes:
            xs, ys = shape.get_points()
            plt.scatter(xs, ys)

        plt.gca().set_aspect('equal')
        plt.show()

    @property
    def holes(self) -> list:
        return self.__holes

    def set_visibility(self, visibility: bool):
        """Make the object visible or not"""
        self.leaf.visible = visibility
        self.leaf.color = Colors.get_random_color()

    def set_opacity(self, oopacity: float):
        """Set the opacity (see-though ness) of the object
        0 = transparent, 1 = no transparency"""
        self.leaf.opacity = oopacity

    def get_cones(self):
        cones = []
        """Generate cones for all holes"""
        for hole in self.holes:
            print(hole)
            c = Cone(hole, y_value=self.y, height=max(hole.vertical_axis, hole.horizontal_axis) * 0.5)
            c.set_visibility(True)
            c.set_opacity(0.4)
            cones.append(c)
        return cones
