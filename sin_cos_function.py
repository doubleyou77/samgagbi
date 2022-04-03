import turtle as t
import math

t.speed(10)
t.setup(width = 1440, height = 900)
t.hideturtle()
t.color('black')

def line(x1,y1,x2,y2): # 좌표평면 그리는 함수
  t.up()
  t.goto(x1,y1)
  t.down()
  t.goto(x2,y2)
  return

def write(x,y,text): #텍스트 입력
  t.up()
  t.goto(x,y)
  t.down()
  t.write(text)
  return

def move(x, y): # 팬 이동 함수
  t.up()
  t.goto(x, y)
  t.down()

line(-720,0,720,0)
line(0,-720,0,720)

i=-720       #좌표 찍기
while i<=720:
  i=i+90
  line(i,-5,i,5)
  write(i-10,-20,i)

i = -720
while i <= 720:
  i = i+90
  line(-5, i, 5, i)
  write(7, i-5, i)

t.color('red')
move(-720, 0)
for x in range(-360*3, 360*3):
  t.goto(x, 90*math.sin(x*3.14/180))

t.color('blue')
move(-720, 0)
for x in range(-360*3, 360*3):
  t.goto(x, 90*math.cos(x*3.14/180))

t.done()