import module

#어떤 모듈 파일에서 import 해서 쓰겟다 
#하면 module. 이것 생략 가능
#from module import MarkertGoods , add
#from module import *

fish1 = module.MarkertGoods(size=20 , price=500)
fish1.show()

print(module.add(1,5))