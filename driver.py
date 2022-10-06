from ellipse import Ellipse
from leaf import Leaf
import vpython as vp

e = Ellipse(2, 0, 5, 6)
# pointer = vp.arrow(pos=vp.vec(0, 1.5, 0), axis=vp.vec(5, 0, 0), shaftwidth=1)
l = Leaf(e, 0.1, 16)
l.display()
l.plot()


while True:
    pass
