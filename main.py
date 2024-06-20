from flask import Flask
from route_handlers.Auth.UserLoginHandler import UserLoginHandler
from route_handlers.Auth.UserRegisterHandler import UserRegisterHandler
from route_handlers.Auth.UserLostPasswordHandler import UserLostPasswordHandler

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login_get():
    return UserLoginHandler.get()

@app.route('/login', methods=['POST'])
def login_post():
    return UserLoginHandler.post()

@app.route('/register', methods=['GET'])
def register_get():
    return UserRegisterHandler.get()

@app.route('/register', methods=['POST'])
def register_post():
    return UserRegisterHandler.post()

@app.route('/lostpw', methods=['GET'])
def lostpw_get():
    return UserLostPasswordHandler.get()

@app.route('/lostpw', methods=['POST'])
def lostpw_post():
    return UserLostPasswordHandler.post()

if __name__ == '__main__':
    app.run(debug=True)
