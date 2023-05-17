

from turtle import*
import random
dsmau=["blue", "purple","darkorange","cyan","plum","darkkhaki"]

#color("white")
shape("arrow")
speed(10)
pensize(2)
#Ẩn con trỏ turtle
hideturtle()
#screen() là hàm tạo ra cửa sổ turlte. Hàm bgcolor thiết lập màu nền
Screen().bgcolor("white")

def vechuv(size):
	left(35)
	forward(size)
	backward(size)
	right(70)
	forward(size)
	backward(size)
	#Quay con trỏ lại vị trí ban đầu
	left(35)

def canhtuyet(size):
	for x in range(4):	
		forward(size)
		vechuv(size)
	#size*4 để đưa con trỏ về vị trí ban đầu
	backward(size*4)
def bongtuyet(size):
	#6 cánh tuyết, chia làm 6 góc 60 độ, mỗi cánh tuyết 1 màu
	for x in range(6):
		color(random.choice(dsmau))
		canhtuyet(size)
		right(60)
#Số bông tuyết muốn vẽ là 10		
for x in range(10):
	size = random.randint(5,30)
	x = random.randint(-400,400)
	y = random.randint(-400,400)
	#Nhấc bút, nhảy tới 1 tọa độ rồi hạ bút
	penup()
	goto(x,y)
	pendown()
	bongtuyet(size)