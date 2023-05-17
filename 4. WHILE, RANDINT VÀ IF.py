import random
number=random.randint(10,20)

dudoan=int(input("Mai thì thầm vào tai bạn: Nếu anh đoán đúng số mà em đang nghĩ trong khoảng từ 10-20. Em sẽ thưởng cho a, hí hí"))
while dudoan!= number:
	if dudoan>20:
		print("Chọn trong khoảng 10-20 cơ mà, đồ hâm này")
	elif dudoan<10:
		print("Chọn trong khoảng 10-20 cơ mà, đồ hâm này")
	elif dudoan< number:
		print("Anh chọn số nhỏ quá rồi, hihi...")
	else:
		print("Chọn số to thế, dỗi~~ hihi...")
	dudoan= int(input("Anh chọn lại đi..."))
print("Hi anh giỏi thế, phạt em đi nào :)")
