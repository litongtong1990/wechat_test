# -*- coding:utf-8 -*-
import werobot

robot = werobot.WeRoBot(token='testrobot', enable_session=True)

@robot.subscribe
def subscribe(message):
    return '欢迎关注本公众号！'

@robot.handler
def echo(message):
    #return '我是WeRoBot机器人xxxxx'
    return message.content

robot.run(server='cherrypy',host='0.0.0.0',port=80)