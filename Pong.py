import curses

player1 = []
player2 = []
ball = []
ball_dx = 1
ball_dy = 1
score_p1 = 0
score_p2 = 0

screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(screen_height, screen_width, 0, 0)  # create new window 
window.keypad(True)  # enable arrow keys
window.timeout(100)


def createa_ball():
    return [[int(screen_height/2), int(screen_width/2)]]


def create_player(x):
    seg1 = [int(screen_height/2), x]
    seg2 = [int(screen_height/2) - 1, x]
    seg3 = [int(screen_height/2) - 2, x]
    return [seg1, seg2, seg3]


def display_head(object):
    window.addch(object[0][0], object[0][1], curses.ACS_CKBOARD)


def display_tail(tail):
    window.addch(tail[0], tail[1], ' ')


def move_ball(ball, player1, player2):
    global ball_dx, ball_dy
    new_head = [ball[0][0], ball[0][1]]
    if new_head in player1 or new_head in player2:
        ball_dx *= -1
    if new_head[0] <= 0 or new_head[0] >= screen_height - 1:
        ball_dy *= -1
    
    #  Score and reset ball position
    global score_p1, score_p2
    scored = False
    if new_head[1] <= 0:
        score_p1 +=1
        scored = True 
    if new_head[1] >= screen_width - 1:
        score_p2 +=1
        scored = True
    if scored:
        new_head = [int(screen_height/2), int(screen_width/2)]
        screen.addstr(1, int(screen_width/2 - 10), "Player 1: {}, Player 2: {}".format(score_p1, score_p2))
        screen.refresh()
        

    new_head[0] += ball_dy        
    new_head[1] += ball_dx
    ball.insert(0, new_head)
    display_tail(ball.pop())
    display_head(ball)


def main_loop():
    global player1, player2, ball
    ball = createa_ball()
    player1 = create_player(2)
    player2 = create_player(screen_width - 2)

    p1_move = "up"
    p2_move = "up"
    key = None

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        if player1[0][0] <= 1:
            key = curses.KEY_DOWN
        if player1[0][0] >= screen_height - 2:
            key = curses.KEY_UP
        if player2[0][0] <= 1:
            key = curses.KEY_F2
        if player2[0][0] >= screen_height - 2:
            key = curses.KEY_F1

        if key == curses.KEY_UP:
            p1_move = "up"
        if key == curses.KEY_DOWN:
            p1_move = "down"
        if key == curses.KEY_F1:
            p2_move = "up"
        if key == curses.KEY_F2:
            p2_move = "down"

        new_head_p1 = [player1[0][0], player1[0][1]]
        new_head_p2 = [player2[0][0], player2[0][1]]

        if p1_move == "up":
            new_head_p1[0] -= 1
        if p1_move == "down":
            new_head_p1[0] += 1
        
        if p2_move == "up":
            new_head_p2[0] -= 1
        if p2_move == "down":
            new_head_p2[0] += 1
        
        
        if key == curses.KEY_LEFT:
            curses.endwin()
            quit()
        
        player1.insert(0, new_head_p1)
        player2.insert(0, new_head_p2)
        display_tail(player1.pop())
        display_tail(player2.pop())
        display_head(player1)
        display_head(player2)
        move_ball(ball, player1, player2)
        

if __name__ == "__main__":
    main_loop()