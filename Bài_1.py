class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name  
        self.type = type  
        self.capacity = capacity  
        self.items = {}  

    def from_size(self, name: str, type: str, size: int):
        return Store(name, type, size // 2)

    def add_item(self, item_name: str):
        current_quantity = sum(self.items.values())    # tính tổng số lượng các mặt hàng hiện có trong cửa hàng

        if current_quantity < self.capacity:  #kiểm tra xem còn đủ sức chứa để thêm mặt hàng hay không
            if item_name in self.items:
                self.items[item_name] += 1    #nếu mặt hàng đã tồn tại, tăng số lượng của nó
            else:
                self.items[item_name] = 1     #nếu không, đặt số lượng là 1
            return f"{item_name} đã được thêm vào cửa hàng"
        else:
            return "Không đủ sức chứa trong cửa hàng"  

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items and self.items[item_name] >= amount:  #kiểm tra xem mặt hàng có tồn tại và đủ số lượng để xóa hay không
            self.items[item_name] -= amount     # Trừ số lượng cần xóa khỏi số lượng hiện tại của mặt hàng
            if self.items[item_name] == 0:      # Nếu số lượng mặt hàng về 0, xóa mặt hàng khỏi từ điển
                del self.items[item_name]
            return f"{amount} {item_name} đã được xóa khỏi cửa hàng"
        else:
            return f"Không thể xóa {amount} {item_name}"  

    def __repr__(self):
        return f"{self.name} loại {self.type} với sức chứa {self.capacity}"



first_store = Store("First store", "Fruit and Veg", 20)
second_store = first_store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)
print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))