class Leaf:
    """A class to manage a leaf in the animation"""

    def __init__(self, major_axis=10, minor_axis=5, height=0.1, num_holes=3):
        """Create a new instance of Leaf, with a specifice major-axis, minor-axis, height/thickness, and number of holes"""
        self.__major_axis = major_axis
        self.__minor_axis = minor_axis
        self.__height = height
        self.__holes = self.generate_holes(num_holes)

    def generate_holes(self, num_holes: int) -> list:
        """Return a list of "holes" where a hole is a circle shape of datatype vp.Shape"""
        for i in range(num_holes):
            # Repeat for the number of holes needed
    

    @staticmethod
    def point__in_ellipse(ellipse_x, ellipse_y, ellipse_horizontal_axis, ellipse_vertical_axis, point_x, point_y)