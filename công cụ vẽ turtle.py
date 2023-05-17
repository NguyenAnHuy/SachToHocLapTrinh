

#Hàm này giúp tải toàn bộ lệnh turtle về mà ko cần phải gõ "turtle" ở đầu mỗi câu lệnh bạn sử dụng
from turtle	import*
#Set màu sắc mà turtle sd
color("darkorange")
#Set loại turtle vs hình dạng con rùa
shape("turtle")
#Set tốc độ của turtle 1-10
speed(2)
#Độ dày đường kẻ
pensize(5)

for x in range(1,4):
	if x ==1:
		#Hướng đầu tiên của mũi tên là quay sang phải
		forward(150)
		#right ở đây là quay theo chiều kim đồng hồ góc 90 độ
		right(90)
		forward(150)
		right(90)
		forward(150)
		right(90)
		forward(150)
	elif x==2:
		forward(150)
		right(90)
		forward(150)
		left(120)
		forward(150)
		left(120)
		forward(150)
	else:
		#Vẽ hình bát giác
		for y in range(8):
			forward(50)
			right(45)