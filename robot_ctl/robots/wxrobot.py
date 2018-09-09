# coding: utf-8

import logging

from robot_ctl.robots.wxBot.wxbot import WXBot

logger = logging.getLogger(__name__)


class WxRobot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            self.send_file_msg_by_uid("img/1.png", msg['user']['id'])


loginWXBots = {}


def loginWX(wxlist):
    for wx in wxlist:
        bot = WxRobot()
        bot.DEBUG = True
        bot.run()
        loginWXBots[wx] = bot


def getWXGroups(groupname=None):
    groups = {}
    for wx in loginWXBots:
        groups[wx] = loginWXBots[wx].group_list

    return groups


def sendToWxGroup(message):
    for wx in loginWXBots:
        wxbot = loginWXBots[wx]
        groups = wxbot.group_list
        for group in groups:
            wxbot.send_msg(group, message, False)
