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

### Case 1: zszywanie pionowe z przesunięciem z prawej w lewą stronę:
# P7(280, 285, 310, 315)
# P7(320, 325, 350, 355)
# P7(360, 365, 390, 395)
# P7(300, 305, 330, 335)
# P7(340, 345, 370, 375)
# P7(380, 385, 410, 415)
# P7(275, 290, 285, 300)
# P7(395, 410, 405, 420)
# P8(315, 330, 325, 340)

# P9(355, 370, 365, 380)

### Case2 zszywanie poziome z przesunięciem z dołu w górę:
# P7(215, 350, 225, 360)
# P7(355, 370, 365, 380)
# P7(255, 390, 265, 400)
# P7(395, 410, 405, 420)
# P7(220, 225, 250, 255)
# P7(380, 385, 410, 415)

# P9(360, 365, 390, 395)





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