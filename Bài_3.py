class Calculator:
    def add(self, *args):
        return sum(args)  #tính tổng tất cả các đối số và trả về kết quả

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num  #nhân dần từng đối số và lưu kết quả vào biến result
        return result 

    def divide(self, *args):
        result = args[0]   #khởi tạo kết quả bằng giá trị đầu tiên
        for num in args[1:]:
            if num == 0:   #kiểm tra số bị chia là 0
                return "Không thể chia cho 0" 
            result /= num  #chia dần từng đối số vào kết quả
        return result  

    def subtract(self, *args):
        result = args[0]   #khởi tạo kết quả bằng giá trị đầu tiên
        for num in args[1:]:
            result -= num  #trừ dần từng đối số vào kết quả
        return result  


calculator = Calculator()
print(calculator.add(5, 10, 4))           
print(calculator.multiply(1, 2, 3, 5))    
print(calculator.divide(100, 2))          
print(calculator.subtract(90, 20, -50, 43, 7)) \


