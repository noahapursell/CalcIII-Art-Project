import vpython as vp


# Disc Generation Test
circ = vp.shapes.circle(radius=0.5)
rect_path = vp.paths.rectangle(width=4, height=2)

e = vp.extrusion(path=rect_path, shape=circ)



