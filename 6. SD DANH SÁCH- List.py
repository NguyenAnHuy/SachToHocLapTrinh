
danhsach=["tên lửa","hành tinh","thiên thạch","người ngoài hành tinh"]				# List
print(danhsach[0])
danhsach[0]= "thay thế tên lửa"			#Thay thế một phần tử đầu tiên
del danhsach[1]							#Xóa phần tử hành tinh
danhsach.append("Thêm vào Sao kim")		# Thêm phần tử vào cuối ds

for item in danhsach:					#item là tên 1 biến tự đặt chỉ các phần tử có trong ds
	print(item)


# danhsach2=[1,2,3,4]
# danhsach3=danhsach2+danhsach		#Gộp 2 danh sách
# for item in danhsach3:
# 	print(item)


# Danh sách(Tuple) không cho thay đổi giá trị bên trong
danhsach=("tên lửa","hành tinh","thiên thạch","người ngoài hành tinh")
print(type(danhsach))


list=[]
for i in range(0,11):
	list.append(i)
print(list)


# Comprehension
list = [i for i in range(0,11)]
print(list)

list2 = [i for i in range(0,11) if (i%2)==0]
print(list2)     