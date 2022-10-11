from ellipse import Ellipse
from leaf import Leaf
import vpython as vp
from cone import Cone
scene = vp.canvas()
scene.ambient = vp.vec(0.7, 0.7, 0.7)
scene.background = vp.color.cyan

e = Ellipse(0, 0, 10, 10)
e2 = Ellipse(0, 4, 50, 50)
# pointer = vp.arrow(pos=vp.vec(0, 1.5, 0), axis=vp.vec(5, 0, 0), shaftwidth=1)
# l = Leaf(e, y=3)
# l.set_visibility(True)
# l.set_opacity(0.6)
# l.make_cones()

# for hole in l.holes:
#     print(hole)
#     c = Cone(hole, y_value = l.y, height = 2)
#     c.set_visibility(True)
#     c.set_opacity(0.4)

# # l.plot()

p = vp.sphere(radius=0.3, pos=vp.vec(0, 0, 0))

# l = Leaf(e)
# l.set_visibility(True)
# l.set_opacity(0.5)

l2 = Leaf(e2, y=-0.4)
l2.set_opacity(0.5)
l2.set_visibility(True)

# cs = l2.get_cones()
# ls= []
# for c in cs:
#     ls.append(c.get_leaf())
# cs = []
# for l in ls:
#     cs += l.get_cones()
# # c = Cone(e2, y_value=-0.4)
# # c.set_visibility(True)
# # c.set_opacity(0.5)

# # l3 = c.get_leaf()

# # c2 = l3.get_cones()

# # l4 = c2[0]
# l4.get_leaf()
def go_to_depth(leafs, depth):
    if depth is 0:
        return
    cs = []
    for l in leafs:
        cs += l.get_cones()
    
    ls = []
    for c  in cs:
        ls.append(c.get_leaf())
    
    go_to_depth(ls, depth-1)


go_to_depth([l2], 5)



while True:
    pass
