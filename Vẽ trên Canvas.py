
from tkinter import*

print("Hãy bấm và giữ chuột trái, di chuyển chuột quanh màn hình để vẽ")
print("Bấm chọn màu để chọn màu vẽ cho cọ của bạn")
cuaso=Tk()
cuaso.wm_title("HẠ ƠI ANH NHỚ EM...")

canvas=Canvas(cuaso, width=750, height =500, bg="white")
canvas.pack(padx=50, pady=50)

canvas.create_text(300,20, text="Hạ ơi, anh muốn địt nát lồn em", font=("times new roman", 12))

#Đặt 2 giá trị cho 2 biến toàn cục cùng 1 lúc
lastX, lastY= 0, 0
colour = "black"

def hamsechay(event):
	global lastX, lastY
	#Lệnh này theo dõi tọa độ của x và y khi trỏ chuột di chuyển
	lastX = event.x
	lastY = event.y
def clickchuot(event):
	hamsechay(event)
def keochuot(event):
	#Khai báo màu sắc nét vẽ và độ dày nét vẽ
	if colour == "white":
		canvas.create_line(lastX, lastY, event.x, event.y, fill= colour, width=30)
	else:
		canvas.create_line(lastX, lastY, event.x, event.y, fill= colour, width=3)
	#Mã lệnh này lưu vị trí trỏ chuột khi bạn kéo xong
	hamsechay(event)

#Liên kết nhấp chuột trái vào hàm clickchuot	
canvas.bind("<Button-1>", clickchuot)
#Bất kể chuyển động nào của chuột trong khi nhấp chuột trái sẽ liên kết vs hàm kéo chuột
canvas.bind("<B1-Motion>", keochuot)

#Mỗi ô vuông dựa trên tọa độ của x và y [trái(x), trên(y), phải(x), dưới (y)]
black_id=canvas.create_rectangle(10,10,30,30, fill="black")
plum_id=canvas.create_rectangle(10,35,30,55, fill="plum")
cyan_id=canvas.create_rectangle(10,60,30,80, fill="cyan")
darkkhaki_id=canvas.create_rectangle(10,85,30,105, fill="darkkhaki")
white_id=canvas.create_rectangle(10,110,30,130, fill="white")

def chonmauden(event):
	global colour
	colour = "black"
def timnhat(event):
	global colour
	colour = "plum"
def xanhngoc(event):
	global colour
	colour = "cyan"
def darkkhaki(event):
	global colour
	colour = "darkkhaki"
def Xoachu(event):
	global colour
	colour = "white"

canvas.tag_bind(black_id, "<Button-1>",chonmauden)
canvas.tag_bind(plum_id, "<Button-1>", timnhat)
canvas.tag_bind(cyan_id, "<Button-1>", xanhngoc)
canvas.tag_bind(darkkhaki_id, "<Button-1>", darkkhaki)
canvas.tag_bind(white_id, "<Button-1>", Xoachu)


cuaso.mainloop()
