


tudien = {"Người dơi":"giàu sụ","Người sắt":"Có rô bốt","Thần sấm":"Có búa sét"}
print("Value của key Người dơi trong từ điển là")
print(tudien["Người dơi"])
print()
tudien["Người dơi"] = " Thay thế giàu sụ"		#Thay thế giá trị của 1 từ khóa
del tudien["Thần sấm"]							#Xóa từ khóa thần sấm
tudien["Superman"]="biết bay"					#Thêm vào người dơi: biết bay
print(tudien)



TUDIEN={"chúng tôi":"vorag", "tới":"thanz", "trong":"zon", "hòa bình":"argh", "xin chào":"kodar","có thể":"znak", "tôi":"az", "mượn":"lifit", "một vài":"zum", "tên lửa":"upgoman"}

#Chuyển những chữ người dùng đánh vào thành chữ thường, tách một chuỗi thành các phần tử phân tách nhau bằng dấu cách
tuvn= input("Nhập 1 cụm từ tiếng việt cần dịch").lower().split()
#Tạo một danh sách trống
bandich=[]				

#Hàm điều kiện IF-IN
for x in tuvn:
	if x in TUDIEN:					
		#ko có dấu ngoặc kép vì ko phải đang thêm vào 1 chuỗi
		bandich.append(TUDIEN[x])		
	else:
		bandich.append(x)
#liên kết tất cả các từ trong danh sách thành 1 chuỗi, giữa mỗi từ có 1 dấu -
print("Tiếng ngoài hành tinh gọi là:","-".join(bandich))	

#--------------------------------------------------------------------

tudien = {"Người dơi":"giàu sụ","Người sắt":"Có rô bốt","Thần sấm":"Có búa sét"}
print(tudien.keys())
if "Ngọc Mai" not in tudien.keys():
	print('Không có')