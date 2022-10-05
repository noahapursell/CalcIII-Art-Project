from dataclasses import dataclass
import math

@dataclass
class Ellipse:
    """Keep track of data necessary for an ellipse"""
    x_pos: float
    y_pos: float
    horizontal_axis: float
    vertical_axis: float

    @staticmethod 
    def point_in_ellipse(
    ellipse,
    point_x: float, 
    point_y: float) -> bool:
        """Return true if a point, specified by (point_x, point_y) is inside an elipse, specified by
        ellipse_horizontal_axis, ellipse_vertical_axis"""
        return ((point_x ** 2 / ellipse.horizontal_axis ** 2) + (point_y ** 2 / ellipse.vertical_axis ** 2)) < 1.0
    
    @staticmethod
    def ellipse_in_ellipse(internal_ellipse, external_ellipse) -> bool:
        """Return true if all sampled points on the internal ellipse are inside the external ellipse"""
        for angle in range(360):
            # For each degree, see if the point is inside the ellipse
            x = internal_ellipse.x_pos - external_ellipse.x_pos + math.cos(math.radians(angle)) * internal_ellipse.horizontal_axis
            y = internal_ellipse.y_pos - external_ellipse.y_pos + math.sin(math.radians(angle)) * internal_ellipse.vertical_axis

            if not Ellipse.point_in_ellipse(external_ellipse, x, y):
                return False

        return True

    @staticmethod
    def ellipse_intersecting_ellipse(ellipse1, ellipse2) -> bool:
        """Return false if all sampled points on an ellipse are outside another ellipse,
        otherwise return true"""
        for angle in range(360):
            # For each degree, see if the point in ellipse1 is inside ellipse2
            x = ellipse1.x_pos - ellipse2.x_pos + math.cos(math.radians(angle)) * ellipse1.horizontal_axis
            y = ellipse1.y_pos - ellipse2.y_pos + math.sin(math.radians(angle)) * ellipse1.vertical_axis
            if Ellipse.point_in_ellipse(ellipse2, x, y):
                return True
        
        return False