from flask import redirect, url_for, session

class UserLogoutHandler:
    @staticmethod
    def get():
        # Clear the user session
        session.pop('user', None)
        # Redirect to the login page
        return redirect(url_for('login'))
