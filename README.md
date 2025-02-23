# Vercel-Telegram-Webhook

![GitHub Repo stars](https://img.shields.io/github/stars/alfchao/Vercel-Telegram-Webhook) ![GitHub Repo stars](https://img.shields.io/github/forks/alfchao/Vercel-Telegram-Webhook)

[TOC]

功能简单的TG通知机器人

## 部署

### 方式一（推荐）：

1. [fork](https://github.com/alfchao/Vercel-Telegram-Webhook/fork) 此项目。
2. 在 [vercel](https://vercel.com/) 上选择自己克隆的项目，设置环境变量后部署。


## 环境变量说明

| 环境变量名         | 是否必须 | 含义                                         |
| ------------------ | -------- | -------------------------------------------- |
| TELEGRAM_BOT_TOKEN | 是       | telegram bot api token                       |
| SALT               | 否       | 生成sendkey的盐，建议修改为一个复杂点的值    |
| CUSTOM_DOMAINS     | 否       | 自定义的域名，不设置则使用 vercel 的提供域名 |

### 用法

向自己 telegram bot 发送 /sendkey 命令即可获取自己定制链接。务必保存好自己的sendkey。  

1. GET

   在URL末尾加上需要发送的文本即可。

2. POST

   - json body

     URL： https://你的域名/send

     Body:

     ```json
     {
       "sendkey": "自己的sendkey",
       "text": "需要发送的文本"
     }
     ```

     