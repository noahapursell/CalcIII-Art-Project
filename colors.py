from distutils.errors import CCompilerError
import random
import vpython as vp

class Colors:
    ROYAL_BLUE_DARK = vp.vec(11 / 365, 29 / 365, 81 / 365)
    CULTURED = vp.vec(249 / 365, 248 / 365, 248 / 365)
    BLACK = vp.vec(0, 0, 0)
    BLUE_BELL = vp.vec(152 / 365, 147 / 365, 218 / 365)
    RUSSIAN_GREEN = vp.vec(98 / 365, 148 / 365, 96 / 365)

    COLORS = [ROYAL_BLUE_DARK, CULTURED, BLACK, BLUE_BELL, RUSSIAN_GREEN]

    @staticmethod
    def get_random_color():
        """Return a random color from the color palete of the project"""
        return Colors.COLORS[random.randint(0, len(Colors.COLORS) - 1)]