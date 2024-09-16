from room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []  # Danh sách các phòng trong khách sạn
        self.guests = 0  # Tổng số khách trong khách sạn

    @classmethod
    def create_from_stars(cls, stars_count: int):
        # Phương thức tạo khách sạn dựa trên số sao
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        # Thêm phòng vào danh sách phòng
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        # Tìm phòng theo số phòng
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if result is None:
                    self.guests += people  # Cập nhật tổng số khách trong khách sạn
                return result
        return f"Room number {room_number} not found"  # Phòng không tồn tại

    def free_room(self, room_number: int):
        # Tìm phòng theo số phòng
        for room in self.rooms:
            if room.number == room_number:
                result = room.free_room()
                if result is None:
                    self.guests -= room.guests  # Cập nhật tổng số khách trong khách sạn
                return result
        return f"Room number {room_number} not found"  # Phòng không tồn tại

    def print_status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]  # Các phòng còn trống
        taken_rooms = [room.number for room in self.rooms if room.is_taken]     # Các phòng đã chiếm
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(map(str, free_rooms))}")
        print(f"Taken rooms: {', '.join(map(str, taken_rooms))}")
