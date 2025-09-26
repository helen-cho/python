from product import Product
import time, datetime

class Sale(Product):
    def __init__(self, code, name, price, qnt):
        super().__init__(code, name, price)
        self.seq=0
        self.qnt= qnt
        #self.date = datetime.date.today()
        self.date = time.localtime()
        self.sum = self.price * self.qnt

    def dict(self):
        child = super().dict()
        child['seq'] = self.seq
        child['qnt'] = self.qnt
        child['date'] = self.date
        child['sum'] = self.sum
        return child
    
if __name__=='__main__':
    sale = Sale('001', '냉장고', 250, 10)
    sale = sale.dict()
    print(sale)
    #print(f"상품등록일{time.strftime('%Y-%m-%d %H:%M:%S').sale['date']}")