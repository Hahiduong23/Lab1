class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number      # Số phòng
        self.capacity = capacity  # Sức chứa
        self.guests = 0           # Số lượng khách hiện tại trong phòng
        self.is_taken = False     # Trạng thái phòng (đã chiếm hay chưa)

    def take_room(self, people: int):
        # Kiểm tra nếu phòng đã bị chiếm hoặc không đủ sức chứa
        if self.is_taken:
            return f"Room {self.number} is already taken"
        if people > self.capacity:
            return f"Room {self.number} cannot accommodate {people} people"
        
        # Nếu đủ điều kiện, chiếm phòng
        self.guests = people
        self.is_taken = True
        return None  # Trả về None nếu chiếm phòng thành công

    def free_room(self):
        # Kiểm tra nếu phòng chưa bị chiếm
        if not self.is_taken:
            return f"Room {self.number} is not taken"
        
        # Giải phóng phòng
        self.guests = 0
        self.is_taken = False
        return None  # Trả về None nếu giải phóng thành công
