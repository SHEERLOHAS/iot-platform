#########################################################################
# File Name: commands.py
# Author   : ATM006
# mail     : 18829897162@163.com
# Time: 2018年05月04日 星期五 10时10分49秒
#########################################################################
#!/usr/bin/python
#-*- coding:utf8 -*-



from flask import Flask
from flask import request,jsonify
#from flask_pymongo import PyMongo
import json,log,rediser
import requests

urlt = 'http://127.0.0.1:5120/iot/spi/devices/'


def commands_get_process(hardwareId):
    log.logger.info("call : commands_get_process()")
    rpool = rediser.redis_pool
    res = rpool.get(hardwareId)
    if res != None:
        return res
    else:
        res = requests.get(urlt + hardwareId + "/events/")
        res = res.json()
        return jsonify({'result': res})
    #return "call commands_get_process()\n"


def commands_post_process(hardwareId,data):
    log.logger.info("call : commands_post_process()")
    rpool = rediser.redis_pool
    rpool.set(hardwareId, data)
    res = requests.post(urlt + hardwareId + "/events/", request.get_data())
    res = res.json()
    return jsonify({'result': res})
    #return "call commands_post_process()\n"