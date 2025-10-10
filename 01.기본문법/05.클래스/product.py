class Product:
    def __init__(self, code, name, price): #생성자
        self.code=code
        self.name=name
        self.price=price

    def dict(self): #메서드(함수)
        return {'code':self.code,'name':self.name,'price':self.price}
    

if __name__=='__main__':
    p = Product('P01', '냉장고', 250)
    print(p.dict())
    