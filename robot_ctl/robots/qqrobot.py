import logging

from qqbot import QQBot

loginQQBots = {}

logger = logging.getLogger(__name__)


def onInit(bot):
    logger.debug('%s.onInit', __name__)


def onQrcode(bot, pngPath, pngContent):
    logger.debug('%s.onQrcode: %s (%d bytes)', __name__, pngPath, len(pngContent))


def onQQMessage(bot, contact, member, content):
    if content == '--version' and getattr(member, 'uin') == bot.conf.qq:
        bot.SendTo(contact, 'QQbot-' + bot.conf.version)


def onInterval(bot):
    logger.debug('%s.onInterval', __name__)


def onStartupComplete(bot):
    logger.debug('%s.onStartupComplete', __name__)


def onUpdate(bot, tinfo):
    logger.debug('%s.onUpdate: %s', __name__, tinfo)


def onPlug(bot):
    logger.debug('%s.onPlug', __name__)


def onUnplug(bot):
    logger.debug('%s.onUnplug', __name__)


def onExit(bot, code, reason, error):
    logger.debug('%s.onExit: %r %r %r', __name__, code, reason, error)


def getQQGroups(groupname=None):
    groups = {}
    for qq in loginQQBots:
        groups[qq] = loginQQBots[qq].List('group', groupname)

    return groups


def sendToQQGroup(message):
    for qq in loginQQBots:
        bot = loginQQBots[qq]
        groups = bot.List('group')
        if groups:
            for group in groups:
                bot.SendTo(group, message)


def loginQQ(qqlist):
    for qq in qqlist:
        bot = QQBot()
        bot.AddSlot(onInit)
        bot.AddSlot(onQrcode)
        bot.AddSlot(onQQMessage)
        bot.AddSlot(onInterval)
        bot.AddSlot(onStartupComplete)
        bot.AddSlot(onUpdate)
        bot.AddSlot(onPlug)
        bot.AddSlot(onUnplug)
        bot.AddSlot(onExit)
        bot.Login(['-q', qq])
        loginQQBots[qq] = bot
