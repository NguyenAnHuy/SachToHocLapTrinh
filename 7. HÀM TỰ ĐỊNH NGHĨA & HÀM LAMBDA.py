# Hiển thị kết quả phép tính: 0-1-2-3-4-5
def calculator(*input_list,mode):		# Có dấu * nghĩa là đó có thể là 1 list gồm chuỗi hoặc số	
	total =0
	if mode =="+":						# ** kwarg tức là 1 bộ từ điển. 2 cái này có thể ko cấp vào hàm
		for i in input_list:
			total+=i
	if mode =="-":
		for i in input_list:
			total -=i
	return total
print(calculator(1,2,3,4,5, mode="-")) # Phải ghi rõ mode = vì nó sẽ không hiểu tham số thứ 2 bắt đầu từ đâu
# -----------------------------------------------------------------------------------------

## Function name = lambda variable1,variable2: process(variable1,variable2)
bigger = lambda num1, num2: num1 if num1 >= num2 else num2			# Sau dấu : là process

# Để như này thì hiển thị lỗi
# bigger(4,10)
# print(bigger)

# Như này mới ra kết quả
print(bigger(4,10))

getprice = lambda price,tax=1.08: int(price*tax)
getprice(100)
print(getprice(100))
print(getprice(100,1.1))				# Thay biến tax = 1.1

# Sự khác nhau giữa có return và không có return

def no_return(a,b):
	print(a+b)				# Trả về 8
print(no_return(5,3))		# Trả về kết quả None

def has_return(a,b):
	return a+b              # Không trả về cái gì
print(has_return(5,3))		# Trả về 8
