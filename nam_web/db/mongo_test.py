import pymongo

m = {
    "이름" : "홍길동",
    "나이" : 30,
    "거주지" : "서울",
    "키" : 170,
    "몸무게" : 80,
    "프로필사진" : [
        "a.jpb",
        "b.jpb"
    ]
}

m2 = {
    "이름" : "홍길동",
    "나이" : 30,
    "학교" : "놀자대",
    "프로필사진" : [
        "a.jpb",
        "b.jpb"
    ]
}


conn = pymongo.MongoClient('mongodb://dbadmin:passw0rd@192.168.56.1:27017')

db = conn.test
col = db.members
#col.insert(m2)

#results = col.find({"학교":"놀자대" , "나이" :30})

#results = col.find({"$or" : [{"이름":"홍길동"} , {"거주지" : "서울"} , {"학교" : "놀자대"}]})
# $gt $gte

results = col.find({"나이":{"&gt":50 , "&lt" :61}} , {"_id" : False , "이름" : True , "거주지" : True}).skip(1).limit(3)


print(results)

for r in results :
    print(r)