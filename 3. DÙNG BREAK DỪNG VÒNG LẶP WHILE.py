print("Nhanh lên, người ngoài hành tinh đang xâm chiếm đấy")
print("Bạn cần bật hệ thống phòng vệ toàn cầu lên ngay")
print("Hi vọng bạn biết mật khẩu vì tương lai trái đất")
print()
print("------------------------------------------------")
print("		CHÀO MỪNG ĐẾN VỚI PHÒNG VỆ TOÀN CẦU 		")
print("------------------------------------------------")
print()

aliens=2
matkhau="ALIENS"
# Chuyển những gì bạn nhập thành viết hoa
doanmk=input("Xin hãy nhập mật khẩu:  ").upper()		

# Khi gõ mk ko chính xác, chương trình sẽ chạy vòng lặp while đến khi người chơi đoán trúng
while doanmk!=matkhau:	
	print()
	print("Mật khẩu ko chính xác")
	print()

	aliens	= aliens**2
	# Dừng vòng lặp while
	if aliens>7400000000:			
		break
	print("Có",aliens,"người ngoài hành tinh đã xâm nhập trái đất. Hãy thử lại")
	print()
	print("Gợi ý mật khẩu: Thứ đang tấn công chúng ta")
	print()
	doanmk=input("Nhanh nào hãy nhập mật khẩu:  ").upper()
if aliens > 7400000000:
	print("Khôngggggg! Người hành tinh chúng đông hơn hẳn chúng ta. Chúng ta thua rồi")
else:
	print("Hoan hoooo! Chúng ta đã chiến thắng, thế giới được giải cứu rồi!")
