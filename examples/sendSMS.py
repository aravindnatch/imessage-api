import requests

# Set the request parameters
json = {
  'number': 'XXXXXXXXXX',
  'service': 'SMS',
  'message': 'hello from imessage-api!',
  'isFile': 'false'
}

# make the request to the local server
req = requests.post('http://127.0.0.1:33229/sendMessage', json=json)

# print the response
print(req.text)