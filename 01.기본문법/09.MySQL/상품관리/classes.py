class Product:
    def __init__(self):
        self.code=''
        self.name=''
        self.price=0

    def print(self):
        print(f'코드:{self.code}, 상품명:{self.name}, 가격:{self.price:,}원')

class Sale(Product):
    def __init__(self):
        super().__init__()
        self.seq=0
        self.date=''
        self.qnt=0
        self.sum = 0

    def print(self):
        print(f'No:{self.seq}, 코드:{self.code}, 상품명:{self.name}, 판매일:{self.date}')
        print(f'판매가:{self.price:,}원, 수량:{self.qnt}개, 금액:{self.sum:,}원')
        print('-' * 70)

if __name__=='__main__':
    pro=Product()
    pro.code='101'
    pro.name='냉장고'
    pro.price=100
    pro.print()

    sale = Sale()
    sale.seq=1
    sale.code=pro.code
    sale.name=pro.name
    sale.price=99
    sale.date='2025-08-29'
    sale.print()