import json
import logging

from qqbot import QQBot
from qqbot.qqfeed import QQFeed

loginQQBots = {}

logger = logging.getLogger(__name__)


class LoginManage:
    lc = None

    def __init__(self):
        pass

    def onInit(self, bot):
        logger.debug('%s.onInit', __name__)

    def onQrcode(self, bot, pngPath, pngContent):
        logger.debug('%s.onQrcode: %s (%d bytes)', __name__, pngPath, len(pngContent))

    def onQQMessage(self, bot, contact, member, content):
        if content == '--version' and getattr(member, 'uin') == bot.conf.qq:
            bot.SendTo(contact, 'QQbot-' + bot.conf.version)

    def onInterval(self, bot):
        logger.debug('%s.onInterval', __name__)

    def onStartupComplete(self, bot):
        logger.debug('%s.onStartupComplete', __name__)

    def onUpdate(self, bot, tinfo):
        logger.debug('%s.onUpdate: %s', __name__, tinfo)

    def onPlug(self, bot):
        logger.debug('%s.onPlug', __name__)

    def onUnplug(self, bot):
        logger.debug('%s.onUnplug', __name__)

    def onExit(self, bot, code, reason, error):
        logger.debug('%s.onExit: %r %r %r', __name__, code, reason, error)

    def getQQGroups(self, groupname=None):
        groups = {}
        for qq in loginQQBots:
            groups[qq] = loginQQBots[qq].List('group', groupname)
        return groups

    def sendToQQGroup(self, message):
        for qq in loginQQBots:
            bot = loginQQBots[qq]
            groups = bot.List('group')
            if groups:
                for group in groups:
                    bot.SendTo(group, message)

    def loginQQ(self, qqlist):
        qqlistlen = len(qqlist)
        for index in range(qqlistlen):
            qq = qqlist[index]
            bot = QQBot()
            bot.AddSlot(self.onInit)
            bot.AddSlot(self.onQrcode)
            bot.AddSlot(self.onQQMessage)
            bot.AddSlot(self.onInterval)
            bot.AddSlot(self.onStartupComplete)
            bot.AddSlot(self.onUpdate)
            bot.AddSlot(self.onPlug)
            bot.AddSlot(self.onUnplug)
            bot.AddSlot(self.onExit)
            feed = QQFeed()
            feed.feedback(LoginCallback(), LoginCallback.loginFeedback.__name__)
            bot.Login(['-q', qq])
            loginQQBots[qq] = bot
            if self.lc is not None:
                self.lc(index, qqlistlen, 'success')

    def loginCounter(self, lc):
        self.lc = lc


class LoginCallback:
    def __init__(self):
        pass

    def loginFeedback(self, authStatus):
        logger.info(json.dumps(authStatus))
