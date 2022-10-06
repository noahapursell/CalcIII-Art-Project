import vpython as vp
from ellipse import Ellipse
import matplotlib.pyplot as plt
e = vp.shapes.ellipse([1, 0], 2, 2)
s = vp.extrusion(
    path = [vp.vec(0, 0, 0), vp.vec(0, 1, 0)],
    shape=[
        e, 
        vp.shapes.circle([0, 0], 0.99), 
    ])


