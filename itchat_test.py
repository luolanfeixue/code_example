# -*- coding: utf-8 -*- 
#
# Author : hhl <dnrhhl@gmail.com>
#
# Time : 五 22  2 2019 14:11:22
#
#

import itchat
import time

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print("收到一条信息：",msg.text)


if __name__ == '__main__':
    itchat.auto_login()
    time.sleep(5)
    itchat.send("文件助手你好哦", toUserName="filehelper")
    itchat.run()

