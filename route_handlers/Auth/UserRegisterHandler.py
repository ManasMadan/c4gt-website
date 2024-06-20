from flask import render_template, request, redirect, url_for, make_response
import logging
import cloud

class UserRegisterHandler:
    @staticmethod
    def get():
        # Send the registration page
        response = make_response(render_template("userregister.html", user=None))
        response.delete_cookie('user')
        return response

    @staticmethod
    def post():
        user = request.form.get('email')
        password = request.form.get('password')
        logging.info(user)
        logging.info(password)
        if cloud.authenticate.user.user_exists(user):
            # User already exists
            return render_template("userregister-exists.html", user=None, reguser=user)
        cloud.authenticate.user.create_user(user, password)
        response = make_response(render_template("userregister-ok.html", user=user))
        response.set_cookie('user', user)
        return response