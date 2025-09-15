class Product():
    serial_num= 0           # 클래스 변수
    def __init__(self):     
        Product.serial_num +=1   
        self.serial_num=Product.serial_num = None     # 인스턴스 변수
        self.name = None
        
        
tv1 = Product()
tv2 = Product()
tv3 = Product()