from flask import render_template, request, redirect, session, jsonify
import logging
import json
from cloud.storage import firebase_storage as storage

class SaveHandler:
    @staticmethod
    def get():
        if 'user' not in session:
            return redirect('/')

        user = session['user']
        path = f"home/{user}/default.json"

        if not storage.existsItem(path):
            filedata = {
                "user": user,
                "fname": "default",
                "data": "\n"
            }
            storage.putItem(path, json.dumps(filedata))

        entries = [path]
        return render_template("allusersheets.html", entries=entries)

    @staticmethod
    def post():
        if 'user' not in session:
            return redirect('/')

        user = session['user']
        fname = request.form.get('fname')
        sheetstr = request.form.get("data", None)

        path = f"home/{user}/{fname}.json"
        if sheetstr is not None:
            if storage.existsItem(path):
                storage.putItem(path, sheetstr)  
            else:
                storage.putItem(path, sheetstr)

        return jsonify(data="Done")
