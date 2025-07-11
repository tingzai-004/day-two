from turtle import *

from random import randrange

snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0],]
apple_x=randrange(-20,20)*10
apple_y=randrange(-20,20)*10
aim_x=10
aim_y=0
       
def squer(x, y, size, color):
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()

def change(x,y):
    global aim_x,aim_y
    aim_x=x
    aim_y=y



def appleLook():
    clear()
    global apple_x,apple_y
    snake.append([snake[-1][0]+aim_x,snake[-1][1]+aim_y])  # 在蛇头添加一个新方块
    
    snake.pop(0)  # 删除蛇尾巴方块，模拟蛇移动
    
    
    for n in range(len(snake)):
        squer(snake[n][0],snake[n][1],10,"black")
        

    squer(apple_x,apple_y,10,"red")
    update()
    ontimer(appleLook, 300)#每三百毫秒动一下



setup (420, 420, 0, 0)
hideturtle()
tracer(False)  # 延迟调为0
listen()
onkey(lambda:change(0,10),"w")
onkey(lambda:change(0,-10),"s")
onkey(lambda:change(-10,0),"a")
onkey(lambda:change(10,0),"d")
appleLook() # 调用函数绘制苹果
done()
