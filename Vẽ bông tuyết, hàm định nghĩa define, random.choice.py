

from turtle import*
import random
dsmau=["blue", "purple","darkorange","cyan","plum","darkkhaki"]

#color("white")
shape("arrow")
speed(8)
pensize(6)
#Ẩn con trỏ turtle
hideturtle()
#screen() là hàm tạo ra cửa sổ turlte. Hàm bgcolor thiết lập màu nền
Screen().bgcolor("gray")

def vechuv():
	left(35)
	forward(50)
	backward(50)
	right(70)
	forward(50)
	backward(50)
	#Quay con trỏ lại vị trí ban đầu
	left(35)

def canhtuyet():
	for x in range(4):
		if x ==0:
			forward(60)
			vechuv()
		else:	
			forward(30)
			vechuv()
	backward(150)
def bongtuyet():
	#10 cánh tuyết, chia làm 9 góc 45 độ, mỗi cánh tuyết 1 màu. Nếu ko khai báo màu từ trên, sẽ có màu mặc định là đen, nên phần mềm ko bị lỗi
	for x in range(10):
		color(random.choice(dsmau))
		canhtuyet()
		right(36)
bongtuyet()