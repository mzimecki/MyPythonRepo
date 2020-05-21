import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A maze game")
wn.setup(700, 700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

levels = []

level_1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'X  XXXXXXX          XXXXX',
    'X  XXXXXXX  XXXXXX  XXXXX',
    'X       XX  XXXXXX  XXXXX',
    'X       XX  XXX        XX',
    'XXXXXX  XX  XXX        XX',
    'XXXXXX  XX  XXXXXX  XXXXX',
    'XXXXXX  XX    XXXX  XXXXX',
    'X  XXX        XXXX  XXXXX',
    'X  XXX  XXXXXXXXXXXXXXXXX',
    'X         XXXXXXXXXXXXXXX',
    'X                XXXXXXXX',
    'XXXXXXXXXXXX     XXXXX  X',
    'XXXXXXXXXXXXXXX  XXXXX  X',
    'XXX  XXXXXXXXXX         X',
    'XXX                     X',
    'XXX         XXXXXXXXXXXXX',
    'XXXXXXXXXX  XXXXXXXXXXXXX',
    'XXXXXXXXXX              X',
    'XX   XXXXX              X',
    'XX   XXXXXXXXXXXXX  XXXXX',
    'XX    YXXXXXXXXXXX  XXXXX',
    'XX          XXXX        X',
    'XXXX                    X',
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
]

levels.append(level_1)

def setup_up_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            x_coor = -288 + (x * 24)
            y_coor = 288 - (y * 24)
            if character == "X":
                pen.goto(x_coor, y_coor)
                pen.stamp()


pen = Pen()

setup_up_maze(levels[0])

while True:
    pass