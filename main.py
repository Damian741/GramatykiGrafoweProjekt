from util.GraphDrawer import draw_graph
from productions.P1 import P1
from productions.P2 import P2
from productions.P7 import P7
from productions.P8 import P8

P1(0)
P2(5)
P2(10)
P2(15)
P2(25)
P2(20)
P7(35, 50, 45, 60)
P7(95, 70, 105, 80)
P7(40, 45, 90, 95)
P8(60, 65, 70, 75)
# P2(10)

# P2(45)

draw_graph()