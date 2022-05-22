import requests  
import json
url = "http://127.0.0.1:8000/fasttag/fine/"
data = {'data':[{'key1':'val1'}, {'key2':'val2'}]}
headers = {'content-type': 'application/json'}
r=requests.post(url, data=json.dumps(data), headers=headers)
res=r.text
print(res)