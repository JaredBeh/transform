from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = new_matrix()
master = ident(new_matrix())
edges = add_edge(edges,0,0,0,20,10,0)
for n in range(200):
    if(n%2 == 0):
        master = make_translate(10,10,0)
    elif(n%3 == 0):
        master = make_rotZ(142)
    else:
        master = make_scale(2,2,1)
    #master = matrix_mult(make_translate(3,3,0),make_rotZ(11))
    edges = matrix_mult(edges,master)
    draw_lines(edges,screen,color)
    master = ident(new_matrix())

display(screen)
