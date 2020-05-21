class FishCakeMaker:
    def __init__(self,**kwargs):
        self._size = 10
        self._flaver = "팥"
        self._price = 100
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs:
            self._flaver = kwargs.get("flavor")
        if "price" in kwargs:
            self._price = kwargs.get("price")
        pass
    def __del__(self):
        print("삭제되었습니다.")
    def __le__(self,other):
        return self._price < other._price
    def __lt__(self,other):
        return self._price <= other._price
    def __gt__(self , other):
        return self._price > other._price
    def __ge__(self,other):
        return self._price >= other._price
    def __eq__(self,other):
        return self._price == other._price
    def __ne__(self,other):
        return self._price != other._price
    def __str__(self):
        return("<class FishCakeMaker (size={},price={},flavor={})>".format(self._flaver,self._price,self._flaver))

    def show(self):
        print("붕어빵 종류 {}".format(self._flaver))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))

class MarkertGoods(FishCakeMaker):
    def __init__(self,margin=1000,**kwargs):
        super().__init__(**kwargs)
        self._market_price = self._price + margin
    def show(self):
        print(self._flaver,self._market_price)

def add(a,b):
    return a+b

print(__name__)
#다른 파일에서 실행 하면 찍히지 않으나 여기서 수행할경우 찍힌다.
if __name__ == "__main__":
    print(__name__)
    fish1 = MarkertGoods(size=20 , price=500)
    fish1.show
    pass