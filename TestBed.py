import vpython as vp
from ellipse import Ellipse
import matplotlib.pyplot as plt

c = vp.cone(
    pos=vp.vec(0, 0, 0),
    size=vp.vec(2, 2, 0.2), # (height, )
    axis=vp.vec(0, -1, 0)
)
