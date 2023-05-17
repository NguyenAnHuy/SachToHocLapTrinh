# Super class
class Animal:
	def __init__(self,animal_type, tall):
		self.__animal_type = animal_type
		self.__tall = tall
	def get_animal_type(self):
		return self.__animal_type
	def get_tall(self):
		return self.__tall
	animal_type =property(get_animal_type)
	tall = property(get_tall)
# Sub class
class Human(Animal):			# Class con kế thừa từ class Animal
	def __init__(self,human_type, tall):
		super().__init__(human_type, tall)		# Dòng đầu tiên class Animal							# super đại diện cho class mẹ
	def greeting(self):
		return "Hello"

human=Human("Human", 180)
lion = Animal("Lion",50)
print(lion.tall)
print(human.tall)				# Trong class human ko có method lấy ra chiều cao
print(human.greeting())			# Nhưng do là class con của Animal nên...