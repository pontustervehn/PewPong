import turtle
from ball import Ball
import winsound

class Paddle:
    def __init__(self,xpos,ypos,shape,img_gray_ammo, img_ammo):
        self.xpos = xpos
        self.ypos = ypos
        self.score = 0
        self.shape = shape
        self.ammo_state = 0
        self.charging_mode = True
        self.img_gray_ammo = img_gray_ammo
        self.img_ammo = img_ammo
        self.balls = {}

        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape(shape)
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(self.xpos, self.ypos)

    def move_up(self):
        print("paddle_UP: {}".format(self))
        if self.paddle.ycor() < 240:
            y = self.paddle.ycor()
            y += 25
            self.paddle.sety(y)

    def move_down(self):
        if self.paddle.ycor() > -244:
            y = self.paddle.ycor()
            y -= 25
            self.paddle.sety(y)

    def increase_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

    def set_shape(self, img):
        self.paddle.shape(img)

    def load_ammo(self):
        if self.charging_mode and self.ammo_state < 4:
            self.ammo_state += 1
            self.set_shape(self.img_gray_ammo[self.ammo_state-1])

        if self.ammo_state >= 4:
            self.charging_mode = False
            self.set_shape(self.img_ammo[3])

    def shoot(self):
        print("Player: {} shoots.".format(self))
        #player shoots
        if not self.charging_mode and self.ammo_state >= 1:
            winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
            self.ammo_state -= 1
            self.set_shape(self.img_ammo[self.ammo_state-1])
            if self.paddle.xcor() > 0:
                self.balls[(Ball(self.paddle.xcor()-10,self.paddle.ycor(), -1, 0, "blue"))] = None;
                #self.balls.append(Ball(self.paddle.xcor(),self.paddle.ycor(), 1, 0, "red"))
            else:
                self.balls[(Ball(self.paddle.xcor()+10,self.paddle.ycor(), 1, 0, "red"))] = None;
                #self.balls.append(Ball(self.paddle.xcor(),self.paddle.ycor(), -1, 0, "blue"))

        if self.ammo_state < 1:
            self.charging_mode = True
            self.set_shape(self.shape)

