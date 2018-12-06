#이 파일은 원격호스트에 있는 파일입니다.
#이 파일을 로컬호스트로 내려받아봅니다.
from turtle import *
class Ball:
    def __init__(self, color, size, speed):
        # 공의 위치 
        self.x = 0
        self.y = 0
 
        # 공의 속도 벡터
        self.xspeed = speed
        self.yspeed = speed
 
        # 공의 크기
        self.size = size
 
        # 공의 색상
        self.color = color

        self.turtle = Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color, color)
                

    # 메소드 정의 
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.turtle.goto(self.x, self.y)

    def backword(self):
        self.x -= self.xspeed
        self.y -= self.yspeed
        self.turtle.goto(self.x, self.y)
 
 
ball = Ball("red", 2, 1)

while True:
    for i in range(100):
        ball.move()

    for i in range(100):
        ball.backword()


