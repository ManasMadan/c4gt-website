from flask import render_template, request, make_response
import logging
from cloud.authenticate.firebase_auth import register_user  # Use Firebase

class UserRegisterHandler:
    @staticmethod
    def get():
        response = make_response(render_template("userregister.html", user=None))
        response.delete_cookie('user')
        return response

    @staticmethod
    def post():
        email = request.form.get('email')
        password = request.form.get('password')
        logging.info(email)
        logging.info(password)

        try:
            user = register_user(email, password)
            response = make_response(render_template("userregister-ok.html", user=email))
            response.set_cookie('user', email)
        except Exception as e:
            logging.error("Registration failed: %s", str(e))
            # You can check for specific error codes in Firebase if needed
            return render_template("userregister-exists.html", user=None, reguser=email)

        return response
