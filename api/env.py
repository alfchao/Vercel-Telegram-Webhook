#!/usr/bin/python3
# coding:utf-8
"""
@File:   env.py
@Date:   2023/3/30 18:12
@Author: Alfred

"""
import os

TELEGRAM_API_URL = 'https://api.telegram.org'
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
SALT = os.environ.get('SALT', 'Vercel-Telegram-Webhook')
CUSTOM_DOMAINS = os.environ.get('CUSTOM_DOMAINS', '')
VERCEL_URL = os.environ.get('VERCEL_URL', '')
if CUSTOM_DOMAINS:
    SITE_URL = f'https://{CUSTOM_DOMAINS}'
elif VERCEL_URL:
    SITE_URL = f'https://{VERCEL_URL}'
else:
    raise Exception('没有域名，需要设置 CUSTOM_DOMAINS 环境变量')

REC_MSG_URL = f'{SITE_URL}/api'
SEND_MSG_URL = f'{SITE_URL}/send'

BOT_COMMANDS = {
    'start': 'get bot info.',
    'sendkey': 'get your own sendkey. ',
}

TG_API = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}'

TG_SET_WK_URL = f'{TG_API}/setWebhook'

TG_SEND_MSG_URL = f'{TG_API}/sendMessage'

TG_SET_CMD_URL = f'{TG_API}/setMyCommands'
