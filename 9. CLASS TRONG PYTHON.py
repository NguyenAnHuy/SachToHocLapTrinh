class TeamA:
	member=0 # class variable

	def __init__(self, name, age):		# Hàm khởi tạol
		self.name = name
		self.age = age
		TeamA.member += 1
	def get_born_year(self):
		return 2021-self.age

mem1 = TeamA("Ngọc Mai",24)
print("BornYear:" + str(mem1.get_born_year()))
print("Tên:",mem1.name)

mem2 = TeamA("An Huy",27)
print("Number of mem:" + str(TeamA.member))

print("--------------------------------------------------------------1")


# --------------------------------------------------------------
class TeamA:
	member=0 # class variable

	def __init__(self, name, age):
		self.__name = name 						# Tạo private member
		self.__age = age
	def get_name(self):					# Khi tạo private member muốn lấy ra phải viết hàm để lấy nó
		return self.__name
	def get_age(self):
		return self.__age
	def set_name(self,name):
		self.__name = name
	def set_age(self,age):
		self.__age = age

	name =property(get_name,set_name)
	age =property(get_age,get_age)


mem1 = TeamA("Ngọc Mai",24)
print(mem1.get_name())
print(mem1.get_age())

mem1.set_age(25)
mem1.set_name("Ngọc Mai 2")
print(mem1.get_name())
print(mem1.get_age())
print("--------------------------------------------------------------2")
mem1.blood="O"					# Thêm một thuộc tính hay biến nữa
print(mem1.blood)
print("--------------------------------------------------------------3")
def get_blood(self):
	return self.blood
TeamA.get_blood = get_blood			# Thêm 1 method vào class
print(mem1.get_blood())

print("--------------------------------------------------------------4")
print(mem1.name)		# ko cần dùng hàm get_name nữa do đã khai báo property

mem1.name = "Ngọc Mai 3"
print(mem1.name)				# Không gộp hàm print vào bên trên được