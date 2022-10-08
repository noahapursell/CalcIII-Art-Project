from ellipse import Ellipse
from leaf import Leaf
import vpython as vp
from cone import Cone
scene = vp.canvas()
scene.ambient = vp.vec(0.7, 0.7, 0.7)
scene.background = vp.color.cyan

e = Ellipse(0, 0, 1, 1)
# pointer = vp.arrow(pos=vp.vec(0, 1.5, 0), axis=vp.vec(5, 0, 0), shaftwidth=1)
l = Leaf(e, 0.1, 7)
l.set_visibility(True)

for hole in l.holes:
    print(hole)
    c = Cone(hole, 0, height = 2)
    c.set_visibility(True)

# # l.plot()

# c = Cone(e)
# c.set_visibility(True)


while True:
    pass
