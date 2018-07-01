import requests as rq
import json
url = "https://app.zencoder.com/api/v2/jobs/"
key = "cef97ec9aa4f0ed89b2c7c128c3bee98"
headers = {"Zencoder-Api-Key":key, "Content-Type":"application/json"}
payload = {"test": "true","input": "s3://zencodertesting/test.mov"}

sts = rq.get(url, headers = headers)
print(sts)
print(headers)
print(payload)
r = rq.post(url, headers = headers, data = json.dumps(payload))
print(r)
print("HTTP Status:", r.status_code)
print("JSON: ", r.json())

