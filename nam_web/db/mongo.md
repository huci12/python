#설치가이드
#https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition-using-deb-packages
#https://blog.rhostem.com/posts/2018-08-31-mongodb-connection

#service가 망가져서 안올라갈때
#https://joonas.tistory.com/38
#지울때
#https://code-machina.github.io/2019/06/14/Installation-Of-Mongodb-On-Ubuntu18.html

'''
use admin
db.createUser( { user: "dbadmin",
  pwd: "passw0rd",
  roles: [ "userAdminAnyDatabase",
  "dbAdminAnyDatabase",
  "readWriteAnyDatabase"
] } )


출처: https://privatecoding.tistory.com/2 [Private Coding]
'''
'''
use myDB db.createUser( { user: "myUserAdmin", pwd: "abc123", roles: [ { role: "dbAdminAnyDatabase", db: "admin" } ] } ) 
use myDB db.createUser( { user: "dbadmin", pwd: "abc123", roles: [ { role: "dbAdminAnyDatabase", db: "admin" } ] } ) 
'''


'''
사용db admin
dbadmin / passw0rd
'''
