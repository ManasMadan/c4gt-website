from cloud.authenticate.firebase_auth import login_user, register_user

def user_exists(email):
    # Firebase doesn't expose this, but for simplicity:
    return False

def create_user(email, password):
    try:
        register_user(email, password)
        return True
    except:
        return False

def authenticate_user(email, password):
    try:
        login_user(email, password)
        return True
    except:
        return False
