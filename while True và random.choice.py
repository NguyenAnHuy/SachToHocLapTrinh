woman = ["Một nhà khoa học","Một nữ hoàng","Một tên cướp biển","Một con thỏ khổng lồ"]
man = ["một sĩ quan cảnh sát","một nghệ sĩ","ông của bạn","một rô bốt sát thủ"]
place = ["trên sao Diêm Vương.","ở siêu thị.","trong 1 cái hang tối tăm ma quái đầy dơi."]
sheWore = ["bộ đồ lặn biển.","cánh tiên.","một cái túi giấy."]
heWore = ["đồ vest tím.","đồ hóa trang cá mập.","khăn tắm đi biển."]
womansay = ["'Anh là ai?'","'Bao nhiêu hạt đậu thì bằng năm?'","'Tại sao?'"]
mansay = ["'Bíp bóp!","'Đừng ăn ếch!'","'Mấy giờ cô sẽ gọi cái này?'"]
consequence = ["hòa bình thế giới.","hỗn loạn.","một bàn chân khổng lồ nghiền nát họ.","cầu vồng."]
worldsaid = ["'Vô nghĩa vớ vẩn!'","'Phô mai là nhất.'","'Tôi đang tan chảy!'"]

import random
while True:		#Câu lệnh này khiến vòng lặp chạy vĩnh viễn		
	print(random.choice(woman),  "gặp", random.choice(man), random.choice(place))
	print("Cô ấy đang mặc", random.choice(sheWore) )
	print("Cô ấy nói:", random.choice(womansay) )
	print("Anh ấy nói:", random.choice(mansay) )			#Chọn 1 phần tử ngẫu nhiên trong DS
	print("Điều đó dẫn đến:", random.choice(consequence) )
	print("Thế giới nói:", random.choice(worldsaid) )

	print()
	input("Ấn Enter để chơi lại")		#Vòng lặp while sẽ tạm dừng cho tới khi người chơi ấn Enter
	print()