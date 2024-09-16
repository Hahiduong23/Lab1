from hotel import Hotel
from room import Room

# Tạo khách sạn 5 sao
hotel = Hotel.create_from_stars(5)

# Tạo các phòng
first_room = Room(1, 3)  # Phòng 1 có sức chứa 3 người
second_room = Room(2, 2)  # Phòng 2 có sức chứa 2 người
third_room = Room(3, 1)   # Phòng 3 có sức chứa 1 người

# Thêm các phòng vào khách sạn
hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

# Cố gắng chiếm phòng
print(hotel.take_room(1, 4))  # Output: Room 1 cannot accommodate 4 people
print(hotel.take_room(1, 2))  # Output: None (thành công)
print(hotel.take_room(3, 1))  # Output: None (thành công)
print(hotel.take_room(3, 1))  # Output: Room 3 is already taken

# Giải phóng phòng
print(hotel.free_room(1))  # Output: None (thành công)
print(hotel.free_room(2))  # Output: Room 2 is not taken

# In trạng thái của khách sạn
hotel.print_status()

