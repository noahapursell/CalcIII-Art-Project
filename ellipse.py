from dataclasses import dataclass
import math
import random
import matplotlib.pyplot as plt


@dataclass
class Ellipse:
    """Keep track of data necessary for an ellipse"""
    x_pos: float
    y_pos: float
    horizontal_axis: float
    vertical_axis: float

    @staticmethod
    def random_ellipse(min_x: float = -5, max_x: float = 5, min_y: float = -5, max_y: float = 5, max_ax: float = 5, min_ax: float = 5):
        """Generate a random ellipse"""
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        ax1 = random.uniform(min_ax, max_ax)
        ax2 = random.uniform(min_ax, max_ax)

        return Ellipse(x, y, ax1, ax2)

    def plot(self, num_points: int = 360):
        xs, ys = self.get_points(num_points)
        plt.plot(xs, ys)
        plt.show()

    def get_points(self, num_points: int = 360):
        """Return two lists, one containing x values, and one containing y values for 
        various points on the ellipse"""
        xs = []
        ys = []

        for i in range(num_points):
            angle = i * 360 / num_points

            x = self.x_pos + \
                math.cos(math.radians(angle)) * self.horizontal_axis
            y = self.y_pos + math.sin(math.radians(angle)) * self.vertical_axis
            xs.append(x)
            ys.append(y)

        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys

    @staticmethod
    def point_in_ellipse(
    ellipse,
    point_x: float,
    point_y: float) -> bool:
        """Return true if a point, specified by (point_x, point_y) is inside an elipse, specified by
        ellipse_horizontal_axis, ellipse_vertical_axis"""
        return (((point_x - ellipse.x_pos) ** 2 / (ellipse.horizontal_axis ** 2)) + ((point_y - ellipse.y_pos) ** 2 / (ellipse.vertical_axis ** 2))) <= 1.0

    @staticmethod
    def ellipse_in_ellipse(internal_ellipse, external_ellipse) -> bool:
        """Return true if all sampled points on the internal ellipse are inside the external ellipse"""
        for angle in range(360):
            # For each degree, see if the point is inside the ellipse
            x = internal_ellipse.x_pos + math.cos(math.radians(angle)) * internal_ellipse.horizontal_axis
            y = internal_ellipse.y_pos + math.sin(math.radians(angle)) * internal_ellipse.vertical_axis

            if not Ellipse.point_in_ellipse(external_ellipse, x, y):
                return False

        return True

    @staticmethod
    def ellipse_intersecting_ellipse(ellipse1, ellipse2) -> bool:
        """Return false if all sampled points on an ellipse are outside another ellipse,
        otherwise return true"""
        for i in range(720):
            angle = i / 2.0
            # For each degree, see if the point in ellipse1 is inside ellipse2
            x = ellipse1.x_pos + math.cos(math.radians(angle)) * ellipse1.horizontal_axis
            y = ellipse1.y_pos + math.sin(math.radians(angle)) * ellipse1.vertical_axis
            if Ellipse.point_in_ellipse(ellipse2, x, y):
                return True

        return False