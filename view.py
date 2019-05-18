# -*- coding: utf-8 -*-
from flask import request, jsonify
import json
from app import app
from configparser import ConfigParser
import logging



@app.route('/start', methods=['GET'])
def start():
    try:
        user = "liangliang"
        session = "0001"
        channel = "wxapp"
        ans = "Hey,I got you!"
        #logger.info({"return": "start", "userId": user, "sessionId": session, "answer": ans, "channel": channel})
        return jsonify({"userId": user, "sessionId": session, "answer": ans, "channel": channel})
    except Exception as e:
        #logger.error(e)
        return jsonify({"state": '400', "message": e})


@app.route('/login', methods=['POST'])
def login():
    try:
        params = json.loads(request.data)
        if params["name"]=="liangliang" and params["password"]=="1234":

            return jsonify({"state":True,"message":"登录成功"})
        else:
            return jsonify({"state": False, "message": "登录失败"})

    except Exception as e:
        #logger.error(e)
        return jsonify({"state": False, "message": e})
