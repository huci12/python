from flask import Flask , Response,render_template,request




app = Flask(__name__)

'''
tiles 설정
http://blog.naver.com/PostView.nhn?blogId=alice_k106&logNo=221375101934&from=search&redirect=Log&widgetTypeCall=true&directAccess=false
'''
'''
extends "default-layout.html" : 이 페이지는 default-layout.html 파일을 상속받아 사용함을 의미한다. default-layout.html
     파일에는 block content ~ endblock 가 코딩되어 있으며, 해당 부분이 index.html의 block content ~ endblock 으로 대체된다.
block content 부터 endblock : 실제로 이 페이지(index.html) 에서 출력할 내용물을 작성한다. 
    위 컨트롤러 파이썬 소스코드에서 넘겨 준 nameValue라는 변수를 jinja2 템플릿 {{ }} 으로 출력하는 간단한 내용을 담고 있다. 
'''

@app.route("/" , methods=["GET"])
def home():
    name="alicek106"
    return render_template("/content/index.html" , nameValue=name)

@app.route("/content/main")
def main():
    return render_template("/content/main.html")

def before_request() :
    app.jinja_env.cache = {}

if __name__=="__main__":
    app.before_request(before_request)
    app.run(host="0.0.0.0",port=8080 , debug=True)