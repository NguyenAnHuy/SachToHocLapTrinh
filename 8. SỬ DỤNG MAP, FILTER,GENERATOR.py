def getPrice(price,tax=1.08):
	return int(price*tax)
prices =[10,20,30,40]
result =[]
result2 =[]

for price in prices:			# Cách làm thông thường, thay từng biến vào hàm. Kết quả trả về là 1 danh sách
	#print(getPrice(price))
	result.append(getPrice(price))
print(result)
print("---------------------1---------------------")

# Map (Function_name, list_name)
for x in map(getPrice, prices):		# x là kết quả khi thay từng biến vào hàm
	print(x)
	result2.append(x)
print(result2)
print("-------------------2----------------------")


result3=list(map(getPrice, prices))		# Trả luôn kết quả về dạng danh sách. Ko cần khai báo rồi append như C2
print(result3)
print("--------------------3---------------------")

# Thay hàm getPrice bằng hàm Lambda
result4= list(map(lambda price, tax=1.08: int(price*tax), prices))	# Dùng hàm lambda thay hàm tự định nghĩa
print(result4)
print("------------------4-----------------------")

result5=[int(price*1.08) for price in prices]			# Viết chương trình trước, biến viết sau
print(result5)
print("-------------------5----------------------")

# --------------print()----------------------------------------------------
def over20(price):								# Hàm điều kiện trả về kq nếu nó >=20
	return price>=20

for j in filter(over20,prices):			# j là kq khi thay từng biến vào hàm
	print(j)
print("-----------------------------------6------")


result3=list(filter(over20, prices))		# Trả luôn kết quả về dạng danh sách
print("result3 =", result3)
print("-----------------------------------7------")

result5=[price for price in prices if price>=20]
print(result5)
print("-----------------------------------8------")
# _________________________________________________________________

days =["thứ hai","thứ ba","thứ bốn","thứ năm","thứ sáu"]
def getday():
	for day in days:
		yield day
w= getday()
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print("reset")
w= getday()
print(next(w))
print(next(w))