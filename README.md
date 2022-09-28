# imessage-api

A simple imessage api that leverages applescript and a local webserver to send iMessage or SMS messages (including files) programmatically. Runs persistently in the macOS menubar.

### Notes

Due to limitations imposed by apple, all features are not available to machines running macOS 10.16 or higher. All macOS versions can send imessages/sms to new or existing conversations.
### Sending a Message
Run the macOS menubar app then run the following code to send a message
```python
import requests

# set the request parameters
json = {
  'number': 'XXXXXXXXXX', # can also be an iMessage enabled email
  'service': 'iMessage', # can also be set to 'SMS'
  'message': 'hello from imessage-api!',
  'isFile': 'false'
}

# make the request to the local server
req = requests.post('http://127.0.0.1:33229/sendMessage', json=json)

# print the response
print(req.text) # {"status":"success","time":"2022-09-26 22:24:54"}
```

### Run/Build Locally

```bash
# clone the repository
git clone https://github.com/aravindnatch/imessage-api.git

# install the dependencies
pip install flask rumps py2app

# run the app locally
python3 main.py

# build the app locally
python3 setup.py py2app
```
