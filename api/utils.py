#!/usr/bin/python3
# coding:utf-8
"""
@File:   utils.py
@Date:   2023/3/30 17:34
@Author: Alfred

"""
import json

import requests

from api.env import *


def json_p(text):
    print(json.dumps(text, ensure_ascii=False, indent=4))


def set_webhook():
    data = {
        'url': REC_MSG_URL
    }
    rep = requests.post(TG_SET_WK_URL, json=data)
    print(f'设置webhook结果， {rep.json()}')


def set_bot_commands():
    command_list = [{
        "command": k,
        "description": v
    } for k, v in BOT_COMMANDS.items()]
    data = {
        "commands": command_list
    }
    rep = requests.post(TG_SET_CMD_URL, json=data)
    json_p(rep.json())


def send_message(chai_id, text, message_id=None):
    data = {
        'chat_id': chai_id,
        'text': text
    }
    if message_id:
        data['reply_to_message_id'] = message_id
    json_p(data)
    rep = requests.post(TG_SEND_MSG_URL, json=data)
    json_p(rep.json())
    return rep.json()

