


from tkinter import *
#Tạo cửa sổ tkinter, đặt tên cho nó, set kích thước
cuaso=Tk()
cuaso.wm_title("MAI ƠI ANH YÊU EM...")
cuaso.geometry('600x400')

Tieude1 = Label(cuaso, text = "Mai ơi em đẹp quá!",font=("Arial Bold", 10))
Tieude1.grid(row = 0, column = 0)

#Biến toàn cục
demclick=0
def hamsechay():
	global demclick
	demclick= demclick+1
	if demclick==1:
		nutbam.configure(text="Anh lừa em đúng ko >.<")
		Tieude1.configure(text="Anh chỉ nói ra sự thật thôi")
	elif demclick==2:
		nutbam.configure(text="Thật ra em cũng đã yêu anh từ lâu rồi")
		Tieude1.configure(text="Anh không ngờ em lại xinh đẹp đến như vậy!!")
	else:
		#Xóa nút bấm
		nutbam.grid_forget()

#Tạo nút bấm, màu nền và màu chữ, hàm nào sẽ chạy nếu nhấn nút, và lưới tọa độ
nutbam=Button(cuaso, text = "Anh nói thật chứ?", width=40, height = 2, bg="white", fg="black", command=hamsechay)
nutbam.grid(row=1,column=10)
#Thêm khoảng trống tính từ nút trở ra theo trục xy
#nutbam.pack(padx=500, pady=500)

cuaso.mainloop()