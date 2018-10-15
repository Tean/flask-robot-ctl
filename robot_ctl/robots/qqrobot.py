import json
import logging
import threading
import time

from qqbot import QQBot
from qqbot.qqfeed import QQFeed

from robot_ctl.singleton import Singleton

loginQQBots = {}
loginQRcode = {}

logger = logging.getLogger(__name__)


class LoginManage():
    __metaclass__ = Singleton

    lc = None

    def __init__(self):
        pass

    def onInit(self, bot):
        logger.debug('%s.onInit', __name__)

    def onQrcode(self, bot, pngPath, pngContent):
        logger.debug('%s.onQrcode: %s (%d bytes)', __name__, pngPath, len(pngContent))

    def onQQMessage(self, bot, contact, member, content):
        from robot_ctl.wsioserver import send_all
        send_all({'member': member.name, 'content': content})
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

    def sendToQQGroup(self, message, groupname=None):
        for qq in loginQQBots:
            bot = loginQQBots[qq]
            if groupname is None:
                groups = bot.List('group')
            else:
                groups = bot.List('group', groupname)
            if groups:
                for group in groups:
                    bot.SendTo(group, message)

    def loginQQs(self, qqlist):
        qqlistlen = len(qqlist)
        for index in range(qqlistlen):
            qq = qqlist[index]
            self.loginQQ(qq)

    def loginQQ(self, qqNo):
        def func(qq):
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
            feed = QQFeed(qq)
            feed.feedback(LoginCallback(), LoginCallback.loginFeedback.__name__)
            feed.qrback(QRCallback(), QRCallback.qrCode.__name__)
            bot.Login(['-q', qq])
            loginQQBots[qq] = bot
            bot.Run()
            if self.lc is not None:
                ql = len(loginQQBots)
            self.lc(loginQQBots, loginQQBots, 'success')

        t = threading.Thread(target=func, args=(qqNo,))
        t.daemon = True
        t.start()

        time.sleep(5)
        return loginQRcode[qqNo]


    def loginCounter(self, lc):
        self.lc = lc


class LoginCallback:
    def __init__(self):
        pass

    def loginFeedback(self, qq, authStatus):
        logger.info(json.dumps(authStatus))


class QRCallback:
    def __init__(self):
        pass

    def qrCode(self, qq, qrcode):
        loginQRcode[qq] = qrcode
        logger.info(qrcode)
