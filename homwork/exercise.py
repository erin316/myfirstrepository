class Xiaoming:
    """
    小明卖瓜，其行为为买进，卖出，算利润
    """
    def __init__(self,base_money=1000):
        self.base_money=base_money
        self.total_purchase_profits=0
        self.total_sale_profit=0
    def purchase(self,fruit,count):
        """
        小明买进水果
        :param fruit: 水果对象
        :param count:  int 购买数量
        """
        fruit.repertory+=count
        if self.base_money-self.total_purchase_profits+self.total_sale_profit-\
                (fruit.pur_price*count)<0:
            raise Exception("小明没钱啦")
        self.total_purchase_profits += fruit.pur_price * count
    def sale(self,fruit,qty):
        """
        小明卖出水果
        :param fruit: 水果对象
        :param qty: int 卖出数量
        """
        fruit.display()
        fruit.repertory-=qty
        self.total_sale_profit+=qty*fruit.sale_price
    def get_total_profit(self):
        """
        计算利润
        :return: float 总利润
        """
        print( self.base_money-self.total_purchase_profits+self.total_sale_profit)


class Fruit:
    """
    父类--抽象的水果类
    """
    def __init__(self,repertory,pur_price,sale_price):
        self.repertory=repertory
        self.pur_price=pur_price
        self.sale_price=sale_price
    def display(self):
        pass

class Apple(Fruit):
    """
    子类--苹果
    """
    def __init__(self,repertory, pur_price, sale_price,name):
        super().__init__(repertory, pur_price, sale_price)
        self.name=name

    def display(self):
        """
        苹果被已榨了汁后被摆摊卖
        """
        print(f"{self.name}苹果正在被榨了汁灌在瓶子里面卖")

class Cherry(Fruit):
    """
    子类--车厘子
    """
    def __init__(self, repertory, pur_price, sale_price,name):
        super().__init__(repertory, pur_price, sale_price)
        self.name=name
    def display(self):
        """
        车厘子被直接摆在地摊卖
        """
        print(f"{self.name}车厘子正在被摆在蓝子卖")

xiaoming=Xiaoming()
apple=Apple(50,10,12,"红富士")
cherry=Cherry(80,13,15,"车厘子")
xiaoming.purchase(apple,50)
xiaoming.purchase(cherry,10)
xiaoming.sale(apple,10)
xiaoming.sale(cherry,10)
xiaoming.get_total_profit()