import turtle
tao = turtle.Pen()# ดึงความสามารถการใช้ปากกา
tao.shape('turtle') # แปลงร่างเป็นเต่า

def Rectangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)


def Go(x,y):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()


Go(200,200)
Rectangle()
