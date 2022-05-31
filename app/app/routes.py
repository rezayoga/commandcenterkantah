from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask 123!"


@app.route('/mysqlconnect')
def mysqlconnect():
    return "mysqlconnect"
