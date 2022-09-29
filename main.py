from threading import Thread
from flask import Flask, request, render_template
from datetime import datetime
import subprocess
import platform
import rumps
import socket
import uuid
import pyperclip

APP_PORT = 33229
API_KEY = ''

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
port = APP_PORT
s.close()

v = platform.mac_ver()[0]
v = float('.'.join(v.split('.')[:2]))
compatible = True if v <= 10.15 else False

mcount = 0
messageCountItem = rumps.MenuItem('Messages: ' + str(mcount))

if API_KEY == '':
  try:
    with open('data/messages.txt') as f:
      lines = f.readlines()
      API_KEY = lines[0].strip()
  except:
    API_KEY = str(uuid.uuid4())
    with open('data/messages.txt', 'w+') as f:
      f.write(API_KEY)

RumpApp = rumps.App(name="imessage-api", icon='assets/icon.png')
RumpApp.menu = [
    messageCountItem,
    None, 
    rumps.MenuItem('IP: ' + ip),
    rumps.MenuItem('Port: ' + str(port)),
    rumps.MenuItem('copy api key', callback=lambda _: pyperclip.copy(API_KEY)),
    None
]

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
  return 'imessage-api <a href="https://github.com/aravindnatch/imessage-api">usage</a>'

@app.route("/sendMessage", methods=['GET','POST'])
def sendMessage():
  content = request.get_json()
  apikey = str(content.get('apikey'))
  number = str(content.get('number'))
  service = str(content.get('service', 'iMessage'))
  message = str(content.get('message'))
  isFile = str(content.get('isFile', 'false')).lower()

  global mcount
  mcount += 1
  messageCountItem.title = 'Messages: ' + str(mcount)

  ret = {
    'status': 'error'
  }

  if apikey == API_KEY:
    if number and message:
      try:
        if compatible:
          subprocess.run(["osascript", "applescript/sendMessage.applescript", number, service, message, isFile])
        else:
          subprocess.run(["osascript", "applescript/legacySendMessage.applescript", number, service, message, 'false'])
        ret['status'] = 'success'
      except Exception as e:
        ret['errormsg'] = str(e)
    else:
      ret['errormsg'] = 'missing either number or message'

    ret['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  else:
    ret['errormsg'] = 'invalid api key'
  
  return(ret)

def runner():
  app.run(port=APP_PORT, host='0.0.0.0')

if __name__ == '__main__':
  thread = Thread(target=runner)
  thread.start()
  RumpApp.run()