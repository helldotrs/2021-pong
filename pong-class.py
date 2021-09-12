#### #### #### import

from pygame import *


#### #### #### class

class MyScreen:
    def __init__(s,screenwidth,screenheight):
        s.SCRN_W    = screenwidth
        s.SCRN_H    = screenheight
        s.screen    = display.set_mode((s.SCRN_W, s.SCRN_H))
        s.CENTER_X  = s.SCRN_W / 2
        s.CENTER_Y  = s.SCRN_W / 2

my_screen           = MyScreen(900,600)


class Color:
    def __init__(s):
        s.WHITE     = (255,255,255)
        s.BLUE      = (50,100,230)  #not used in current version
        s.RED       = (230,0,100)   #--ll--
        s.BLACK     = (0,0,0)
        s.BG_COLOR  = s.BLACK

color               = Color()


class Player:
    def __init__(s, y, x, paddle_width, paddle_height, key_up, key_down, color, paddle_speed, score):
        s.y         = y
        s.X         = x
        s.paddle_w  = paddle_width
        s.paddle_h  = paddle_height
        s.key_up    = key_up
        s.key_down  = key_down
        s.COLOR     = color
        s.paddle_s  = paddle_speed
        s.score     = score

p1                  = Player(250, 50,   30, 100, K_w,   K_s,    color.WHITE, 5, 0)
p2                  = Player(250, 850,  30, 100, K_UP,  K_DOWN, color.WHITE, 5, 0)


class Ball:
    def __init__(s, x, y, speed, SIZE, color):
        s.x         = x
        s.y         = y
        s.speed     = speed #keep constant rather than var for future game-modes
        s.SIZE      = SIZE
        s.dx        = s.speed
        s.dy        = s.speed
        t.color     = color

ball                = Ball(my_screen.CENTER_X, my_screen.CENTER_Y, 4, 10, color.WHITE)


class SysClass():
    def __init__(s):
        font.init()

        s.calibri_bold_35   = font.SysFont("Calibri Bold", 35)
        s.output_font       = s.calibri_bold_35
        s.running           = True
        s.my_clock          = time.Clock()
        s.msg               = "" #fuck you josh

sysClass            = SysClass()


#### #### #### main-loop

while sysClass.running:
    for evt in event.get():
        if evt.type == QUIT:
            sysClass.running = False


    pl_paddle   = Rect(p1.X,   p1.y,   p1.paddle_w, p1.paddle_h)
    p2_paddle   = Rect(p2.X,   p2.y,   p2.paddle_w, p2.paddle_h)
    ball_var    = Rect(ball.x, ball.y, ball.SIZE,   ball.SIZE)

    keys        = key.get_pressed()


    #player 1 input
    if   (keys[p1.key_up]   and p1.y>0):
        p1.y    -= p1.paddle_s
    elif (keys[p1.key_down] and p1.y + p1.paddle_h < my_screen.SCRN_H):
        p1.y    += p1.paddle_s


    #player 2 input
    if   (keys[p2.key_up]   and p2.y>0):
        p2.y    -= p2.paddle_s
    elif (keys[p2.key_down] and p2.y + p2.paddle_h < my_screen.SCRN_H):
        p2.y    += p2.paddle_s


    ball.x      += ball.dx
    ball.y      += ball.dy
    if  (ball_var.colliderect(pl_paddle)):              #left paddle collition
        ball.dx =   abs(ball.dx)                        #abs to make positive motion.
    elif(ball_var.colliderect(p2_paddle)):              #right paddle collition
        ball.dx =   abs(ball.dx) * -1                   #abs times -1 for negative motion
    elif(ball.y <=  0):                                 #top of screen collition
        ball.dy =   abs(ball.dy)
    elif(ball.y >=  my_screen.SCRN_H):                  #bottom of screen collition
        ball.dy =   abs(ball.dy) * -1
    elif(ball.x >=  my_screen.SCRN_W or ball.x <= 0):   #goal collition
        if   ball.x     >= my_screen.SCRN_W:
            p1.score   += 1                             #++ does not work in python?
        elif ball.x     <= 0:
            p2.score   += 1
        ball.x =    my_screen.CENTER_X
        ball.y =    my_screen.CENTER_Y
        """
        Majd Hailat suggests to here reset the paddles, I feel that this would
            make the gaming-experience quite discombobulatingand hence I will not.
        """


    my_screen.screen.fill(color.BG_COLOR)
    draw.rect(my_screen.screen, p1.COLOR,   pl_paddle)
    draw.rect(my_screen.screen, p2.COLOR,   p2_paddle)
    draw.rect(my_screen.screen, ball.color, ball_var)
    p1_pts_txt = sysClass.output_font.render(f"{p1.score}", True, p1.COLOR)
    p2_pts_txt = sysClass.output_font.render(f"{p2.score}", True, p2.COLOR)
    bottom_txt = sysClass.output_font.render(sysClass.msg,  True, color.WHITE)
    my_screen.screen.blit(p1_pts_txt, (130, 20))
    my_screen.screen.blit(p2_pts_txt, (620, 20))
    my_screen.screen.blit(bottom_txt, (130, 520))


    display.flip()
    sysClass.my_clock.tick(60)


#### #### #### quit

quit()
