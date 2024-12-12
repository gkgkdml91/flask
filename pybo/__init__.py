from flask import Flask
# app 객체를 전체 전역으로 사용
# 프로젝트 규모가 커질수록 문제가 발생함
# 문제 : 순환 참조 오류

# 방지하기 위한 방법 : 애플리케이션 팩토리
# app = Flask(__name__)

#애플리케이션 팩토리 완성
# create_app() 함수 안에
# app 이라는 Flask 인스턴스를 생성해서 작동하게 함
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app