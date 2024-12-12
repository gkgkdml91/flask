from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')
# url_prefix = '/'
# 밑에 접속하는 주소의 기본값
# 예 ) url_prefix = '/main'
# localhost:5000/main 라고 기본으로 붙어서 나옴

@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!'