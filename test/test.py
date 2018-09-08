# coding: utf-8
import logging

from robot_ctl.robots.qqrobot import getQQGroups
from robot_ctl.robots.wxrobot import loginWX, sendToWxGroup

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(name)s:[%(lineno)d] - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# loginQQ(['3283253806','1411729768'])

loginWX(['wxid_g75tjx6f0fv612'])

key = ''
while key != 'c':
    key = raw_input('wait ...')
    logger.debug(key)
    logger.info(key)
    logger.warn(key)
    logger.error(key)
    logger.fatal(key)
    logger.critical(key)

sendToWxGroup('xxx')
print(getQQGroups())
# sendToGroup('for test')

key = ''
while key != 'q':
    key = raw_input('wait ...')
    print(key)
