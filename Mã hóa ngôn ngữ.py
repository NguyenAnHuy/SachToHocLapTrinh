
vonglap="huy"
while vonglap !="mai":
	bangchucai="ABCDEFGHIJKMNOPQRSTUVWXYZABCDEFGHIJKMNOPQRSTUVWXYZ"
	thongdiep=input("Nhập thông điệp cần mã hóa:").upper()
	somakhoa=input("Nhập một số từ 1-25 để làm mã khóa:")

	#Tạo một chuỗi rỗng
	bandich= ""			


	for x in thongdiep:
		if x in bangchucai:
			#Tìm kiếm ở bảng chữ cái mỗi lần ký tự trong thongdiep xuất hiện, và gửi về index của ký tự ấy
			index=bangchucai.find(x)
			indexmahoa=index + int(somakhoa)
			#thêm chữ cái sau mã hóa vào bản dịch. Gộp 2 chuỗi
			bandich=bandich+bangchucai[indexmahoa]
		else:
			bandich= bandich+ x
	print(bandich)