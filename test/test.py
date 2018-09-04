import logging

from robot_ctl.robots.qqrobot import loginQQ, getGroups, sendToGroup

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

loginQQ(['3283253806'])

print(getGroups())

sendToGroup('for test')