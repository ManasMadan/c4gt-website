from flask import render_template, request, redirect, make_response, session
import logging
from cloud.authenticate.firebase_auth import login_user  # Use Firebase-based login

class UserLoginHandler:
    @staticmethod
    def get():
        session.pop('user', None)
        return render_template("userlogin.html", user=None)

    @staticmethod
    def post():
        email = request.form.get('email')
        password = request.form.get('password')
        logging.info(email)
        logging.info(password)

        try:
            user = login_user(email, password)
            logging.info("Firebase authentication succeeded")
            session['user'] = user['email']
            return redirect('/save')
        except Exception as e:
            logging.error("Firebase authentication failed: %s", str(e))
            return render_template("userlogin.html", user=None, error="Invalid email or password")
