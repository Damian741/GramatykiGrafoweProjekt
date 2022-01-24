from pytest import fixture

from productions import *


@fixture
def basic_graph_for_P9 () -> None:
    P1 (0)
    P2 (5)
    P2 (10)
    P2 (15)
    P2 (25)
    P2 (20)
    P7 (35, 50, 45, 60)
    P7 (95, 70, 105, 80)
    P7 (40, 45, 90, 95)
    P8 (60, 65, 70, 75)
    P2 (30)
    P2 (35)
    P2 (40)
    P2 (45)
    P2 (90)
    P2 (95)
    P2 (100)
    P2 (105)
    P2 (50)
    P2 (55)
    P2 (60)
    P2 (65)
    P2 (70)
    P2 (75)
    P2 (80)
    P2 (85)


@fixture
def merge_horizontal__shift_up__graph (basic_graph_for_P9) -> None:
    P7 (215, 350, 225, 360)
    P7 (355, 370, 365, 380)
    P7 (255, 390, 265, 400)
    P7 (395, 410, 405, 420)
    P7 (220, 225, 250, 255)
    P7 (380, 385, 410, 415)


@fixture
def merge_vertical__shift_left__graph (basic_graph_for_P9) -> None:
    P7 (280, 285, 310, 315)
    P7 (320, 325, 350, 355)
    P7 (360, 365, 390, 395)
    P7 (300, 305, 330, 335)
    P7 (340, 345, 370, 375)
    P7 (380, 385, 410, 415)
    P7 (275, 290, 285, 300)
    P7 (395, 410, 405, 420)
    P8 (315, 330, 325, 340)