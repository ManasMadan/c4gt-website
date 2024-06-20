from flask import render_template, request, redirect, url_for, make_response
import logging
import cloud

class UserLoginHandler:
    @staticmethod
    def get():
        response = make_response(render_template("userlogin.html", user=None))
        response.delete_cookie('user')
        return response

    @staticmethod
    def post():
        # Verify user login
        user = request.form.get('email')
        password = request.form.get('password')
        logging.info(user)
        logging.info(password)
        if cloud.authenticate.user.authenticate_user(user, password):
            logging.info("authenticate succeeded")
            response = redirect(url_for('save'))
            response.set_cookie('user', user)
        else:
            logging.info("authenticate failed")
            response = redirect(url_for('login_get'))
        return response
