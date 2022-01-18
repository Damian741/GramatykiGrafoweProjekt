from util.GraphDrawer import draw_graph
from productions.P1 import P1
from productions.P2 import P2
from productions.P7 import P7
from productions.P8 import P8
from productions.P9 import P9
from common import *

P1(0)
P2(5)
P2(10)
P2(15)
P2(25)
P2(20)
# Stage for P9:
P7(35, 50, 45, 60)
P7(95, 70, 105, 80)
P7(40, 45, 90, 95)
P8(60, 65, 70, 75)
P2(30)
P2(35)
P2(40)
P2(45)
P2(90)
P2(95)
P2(100)
P2(105)
P2(50)
P2(55)
P2(60)
P2(65)
P2(70)
P2(75)
P2(80)
P2(85)
P7(280, 285, 310, 315)
P7(320, 325, 350, 355)
P7(360, 365, 390, 395)
P7(300, 305, 330, 335)
P7(340, 345, 370, 375)
P7(380, 385, 410, 415)
P7(275, 290, 285, 300)
P7(395, 410, 405, 420)
P8(315, 330, 325, 340)


vgf = verticies_graph_fragment
gfl = graph_fragment_list
id1 = 355
id2 = 370
id3 = 365
id4 = 380
P9(id1, id2, id3, id4)

uL = vgf.get(id1)
uR = vgf.get(id2)
lL = vgf.get(id3)
lR = vgf.get(id4)

# upper Left z upper Right (355 i 370)
set(uL.vertices).isdisjoint(uR.vertices)
# upper Left z lower Left (355 i 365)
set(uL.vertices).isdisjoint(lL.vertices)
# upper Right z lower Right (370 i 380)
set(uR.vertices).isdisjoint(lR.vertices)
# lower Left z lower Right (370 i 380)
set(lL.vertices).isdisjoint(lR.vertices)

set(lL.vertices).isdisjoint(uR.vertices)

def pp(l):
    for i in l:
        print(f"x: {i.x}, y {i.y}, id {i.id}")


#P8(355, 370, 365, 380)

# 1 case
# P7(35, 50, 45, 60)
# P7(95, 70, 105, 80)
# P7(40, 45, 90, 95)
# P8(60, 65, 70, 75)
# 2 case
# P7(35, 50, 45, 60)
# P7(95, 70, 105, 80)
# P7(60, 65, 70, 75)
# P8(40, 45, 90, 95)
# 3 case
# P7(40, 45, 90, 95)
# P7(60, 65, 70, 75)
# P7(95, 70, 105, 80)
# P8(35, 50, 45, 60)
# 4 case
# P7(40, 45, 90, 95)
# P7(60, 65, 70, 75)
# P7(35, 50, 45, 60)
# P8(95, 70, 105, 80)

draw_graph()