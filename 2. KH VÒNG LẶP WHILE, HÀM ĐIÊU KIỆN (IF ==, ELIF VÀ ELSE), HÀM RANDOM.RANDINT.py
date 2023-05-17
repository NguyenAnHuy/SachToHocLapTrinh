import random

luachon_thoat="ko co gi"
# Khi lựa luachon_thoat ko bằng "thoat" chuong trinh vẫn sẽ chạy tiếp
while luachon_thoat!="Thoat":

	print("Bạn đang trong một căn phòng tối tăm nằm trong một lâu đài bí hiểm.")
	print("Có 3 cánh cửa trước mặt bạn. Hãy chọn 1 cánh cửa để thám hiểm.")
	luachon=input("Hãy chọn 1,2,3 hoặc 4...")
	if luachon=="1":
		print("Bạn đã tìm thấy căn phòng chứa kho báu. Phát tài rồi!")
		print("Bạn đã thắng cuộc. Trò chơi kết thúc.")
	elif luachon=="2":
		print("Cửa bật mở. Một tiểu yêu lao ra phang chùy vào đầu bạn.")
		print("Bạn đã thua. Trò chơi kết thúc.")
	elif luachon=="3":
		print("Bạn bước vào căn phòng và thấy một con rồng đang ngủ say.")
		print("Bạn có thể")
		print("1) Thử trộm vàng của con rồng")
		print("2) Thử đi vòng qua con rồng")
		luachon_rong=input("Điền 1 hoặc 2 ")
		if luachon_rong=="1":
			print("Con rồng thức giấc và nuốt chửng bạn luôn. Ái chà ngon quá!")
			print("Bạn đã thua")
		elif luachon_rong=="2":
			print("Bạn lén đi qua con rồng và thoát khỏi tòa lâu đài")
			print("Bạn đã thắng cuộc. Trò chơi kết thúc.")
		else:
			print("Xin lỗi bạn đã không lựa chọn 1 hoặc 2")
	elif luachon=="4":
		print("Căn phòng bạn bước vào có một con nhân sư")
		print("Nhân sư bắt bạn đoán con số nó đang nghĩ đến, nó nằm trong khoảng từ 1 đến 10")
		luachon_nhansu=int(input("Bạn chọn số nào"))
		if luachon_nhansu==random.randint(1,2):
			print("Nhân sư gầm lên thất vọng, bạn đã trả lời đúng")
			print("Nhân sư phải thả bạn đi")
			print("Bạn đã chiến thắng, trò chơi kết thúc")
		else:
			print("Nhân sư nói đáp án của bạn ko chính xác")
			print("Bạn đã trở thành tù nhân của nó mãi mãi")
			print("Bạn đã thua trò chơi kết thúc")
	else:
		print("Xin lỗi bạn đã không lựa chọn 1, 2,,3 hoặc 4!")
	luachon_thoat=input("Ấn ENTER để chơi lại hoặc gõ 'Thoat' để thoát trò chơi")
