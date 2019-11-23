#!/usr/bin/env python3

import gifmaze as gm
from gifmaze.algorithms import prim

def gif_1():
    surface = gm.GIFSurface(width=600,height=600,bg_color=0)
    surface.set_palette([0,0,0,255,255,255,255,0,255,0,0,0])
    anim =gm.Animation(surface)
    maze = gm.Maze(149,99,None).scale(4).translate((2,2))
    anim.run(prim,maze,speed=30,delay=5,trans_index=None,cmap={0:0,1:1},start=(0,0))
    surface.save('qqq.gif')
    surface.close()
#gif_1()

sat = '1,2,5,3,49,66,1,8'
print(f'是{sat}列表')
print('是%s列表' %sat)