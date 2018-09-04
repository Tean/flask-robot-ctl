import logging

from robot_ctl.robots.qqrobot import loginQQ, getGroups, sendToGroup

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(name)s:[%(lineno)d] - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# loginQQ(['3283253806'])

loginQQ(['1411729768'])

key = ''
while key != 'c':
    key = raw_input('wait ...')
    logger.debug(key)
    logger.info(key)
    logger.warn(key)
    logger.error(key)
    logger.fatal(key)
    logger.critical(key)

print(getGroups())
# sendToGroup('for test')

key = ''
while key != 'q':
    key = raw_input('wait ...')
    print(key)
