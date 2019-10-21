import turtle
import random
import math
import winsound
from imagehandler import *

class Ball:
    def __init__(self,xpos=0,ypos=0, dx=1, dy=1, color="white"):
        self.xpos = xpos
        self.ypos = ypos
        self.main = False

        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color(color)
        self.ball.penup()
        self.ball.goto(self.xpos, self.ypos)
        self.ball.dx = dx
        self.ball.dy = dy

#TODO fix speed
    def move(self):
        #self.ball.dx = dx
        #self.ball.dy = dy
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def set_main(self):
        self.main = True

    def reset_ball_pos(self,launch_towards):
        self.ball.sety(0)
        self.ball.setx(0)

        if launch_towards == "a":
            a_r = [[160, 180], [180, 200]]
            a_r_choice = a_r[random.randint(0, 1)]
            random_angle = math.radians(random.randint(a_r_choice[0], a_r_choice[1]))
        else:
            a_r = [[0, 20],[340, 360]]
            a_r_choice = a_r[random.randint(0, 1)]
            random_angle = math.radians(random.randint(a_r_choice[0], a_r_choice[1]))

        #print("Angle: {}".format(random_angle))
        #print("Cos: {}, Sin: {}".format(math.cos(random_angle), math.sin(random_angle)))
        self.ball.dx = math.cos(random_angle)
        self.ball.dy = math.sin(random_angle)

    def check_collisions_border(self, paddle_a, paddle_b, score):
        if self.ball.ycor() > 290:
            winsound.PlaySound("wall_bounce.wav", winsound.SND_ASYNC)
            self.ball.sety(290)
            self.ball.dy *= -1

        if self.ball.ycor() < -280:
            winsound.PlaySound("wall_bounce.wav", winsound.SND_ASYNC)
            self.ball.sety(-280)
            self.ball.dy *= -1

        #ball hits left or right sides and resets in the middle
        if self.ball.xcor() > 390:
            #paddle a scored on paddle b
            #winsound.PlaySound("playerascores.wav", winsound.SND_ASYNC)
            paddle_a.increase_score(1)
            score.display("Player A: {}  Player B: {}".format(paddle_a.get_score(), paddle_b.get_score()))


            if self not in paddle_a.balls:
                if self not in paddle_b.balls:
                    self.reset_ball_pos("a")
                    #print("paddle A balls: {}".format(paddle_a.balls))
                    #print("paddle A balls: {}".format(paddle_b.balls))
                    #print("self: {}".format(self))
                else:
                    self.ball.reset()
                    del paddle_b.balls[self]
            else:
                #print("trying to delete 1")
                self.ball.reset()
                del paddle_a.balls[self]

        if self.ball.xcor() < -390:
            #paddle b scored on paddle a
            #winsound.PlaySound("playerbscores.wav", winsound.SND_ASYNC)
            paddle_b.increase_score(1)
            score.display("Player A: {}  Player B: {}".format(paddle_a.get_score(), paddle_b.get_score()))

            if self not in paddle_a.balls:
                if self not in paddle_b.balls:
                    self.reset_ball_pos("b")
                else:
                    self.ball.reset()
                    del paddle_b.balls[self]
            else:
                #print("trying to delete 2")
                self.ball.reset()
                del paddle_a.balls[self]


    def check_collisions_paddles(self, paddle_a, paddle_b):
        p_a_y = paddle_a.paddle.ycor()
        p_b_y = paddle_b.paddle.ycor()

        #bounce on paddle B
        if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (self.ball.ycor() < p_b_y + 46 and self.ball.ycor() > p_b_y -45):
            winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
            self.ball.setx(340)
            self.ball.dx *= -1
            if self.main and (self.ball.ycor() < p_b_y + 10 and self.ball.ycor() > p_b_y -10):
                paddle_b.load_ammo()

        #bounce on paddle A
        if (self.ball.xcor() < -340 and self.ball.xcor() > -350) and (self.ball.ycor() < p_a_y + 46 and self.ball.ycor() > p_a_y -45):
            winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
            self.ball.setx(-340)
            self.ball.dx *= -1
            if self.main and (self.ball.ycor() < p_a_y + 10 and self.ball.ycor() > p_a_y -10):
                paddle_a.load_ammo()
