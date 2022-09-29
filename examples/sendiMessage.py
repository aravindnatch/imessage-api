import requests

# Set the request parameters
json = {
  'apikey': 'YOUR_API_KEY',
  'number': 'XXXXXXXXXX',
  'service': 'iMessage',
  'message': 'hello from imessage-api!',
  'isFile': 'false'
}

# make the request to the local server
req = requests.post('http://localhost:33229/sendMessage', json=json)

# print the response
print(req.text)