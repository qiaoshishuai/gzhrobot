# -*- coding=utf-8 -*-
import hashlib
import reply
import receive
import web
import robot #robot.py在之后写即可
class Handle(object):
 def GET(self):
  try:
   data = web.input()
   if len(data) == 0:
    return "hello, this is handle view"
   signature = data.signature
   timestamp = data.timestamp
   nonce = data.nonce
   echostr = data.echostr
   token = "微信公众号上的token值"

   list = [token, timestamp, nonce]
   list.sort()
   sha1 = hashlib.sha1()
   map(sha1.update, list)
   hashcode = sha1.hexdigest()
   if hashcode == signature:
    return echostr
   else:
    return ""
  except Exception as Argument:
   return Argument
 def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            recMsg=receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType=='text':
                    content = recMsg.Content
                    rpyMsg= robot.get_response(content)
                    print rpyMsg
                    replyMsg = reply.TextMsg(toUser, fromUser,rpyMsg)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
            else:
                print("none handler yet")
                return "success"
        except Exception as Argument:
            print Argment
            return "fail"