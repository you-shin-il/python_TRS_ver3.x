import urllib
import urllib.parse
import hashlib
import hmac
import base64
import time
import datetime

baseurl='https://connector.gigagenie.ai/ai/v1/client/api?'
request={}

client_id = 'Y2xpZW50X2lkMTU3MDY3NTM2MDA0Ng=='
client_secret = 'Y2xpZW50X3NlY3JldDE1NzA2NzUzNjAwNDY='
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

request['command'] = 'Translation'
request['transType'] = 'ek'
request['transMsg'] = 'I am the master of my soul'
request['timestamp'] = timestamp
request['client_id'] = client_id
print(timestamp)

request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])
request_str = request_str.replace('+','%20')
client_secret = bytes(client_secret, 'utf-8')
data = bytes(client_id+":"+timestamp, 'utf-8')
sig = hmac.new(client_secret, data, hashlib.sha256).hexdigest()
req=baseurl+request_str+'&signature='+sig

print(req)