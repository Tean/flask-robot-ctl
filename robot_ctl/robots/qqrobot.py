import logging

from qqbot import QQBot

loginBots = {}

logger = logging.getLogger(__name__)

def loginQQ(qqlist):
    for qq in qqlist:
        bot = QQBot()
        bot.Login(['-q', qq])
        loginBots[qq] = bot;


def getGroups():
    groups = {}
    for qq in loginBots:
        groups[qq] = loginBots[qq].List('group')

    return groups


def sendToGroup(message):
    for qq in loginBots:
        bot = loginBots[qq]
        groups = bot.List('group')
        if groups:
            for group in groups:
                bot.SendTo(group, message)


def onStartupComplete(bot):
    logger.info('logged in')