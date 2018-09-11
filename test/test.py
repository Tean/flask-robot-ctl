# coding: utf-8
import logging

from robot_ctl.robots.qqrobot import LoginManage

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(name)s:[%(lineno)d] - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

loginm = LoginManage()


def lc(current, count, status):
    logger.debug("{}[{}]:{}".format(current, status, count))


loginm.loginCounter(lc)

key = ''
while key != 'l':
    key = raw_input('等灯等灯...')
    logger.debug(key)
    logger.info(key)
    logger.warn(key)
    logger.error(key)
    logger.fatal(key)
    logger.critical(key)

loginm.loginQQs(['3283253806', '1411729768'])

# loginWX(['wxid_g75tjx6f0fv612'])

key = ''
while key != 'c':
    key = raw_input('等灯等灯...')
    logger.debug(key)
    logger.info(key)
    logger.warn(key)
    logger.error(key)
    logger.fatal(key)
    logger.critical(key)

# sendToWxGroup('xxx')
print(loginm.getQQGroups())
# sendToGroup('for test')

key = ''
while key != 'q':
    key = raw_input('等灯等灯...')
    print(key)
