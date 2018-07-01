import requests as rq
import json

key="cef97ec9aa4f0ed89b2c7c128c3bee98"
url = "https://app.zencoder.com/api/v2/jobs/"
def create_job(url = url, key= key,
              headers = {"Zencoder-Api-Key":key, "Content-Type":"application/json"},
              payload = {"test": "true","input": "s3://zencodertesting/test.mov"}):
    sts = rq.get(url, headers = headers)
    r = rq.post(url, headers = headers, data = json.dumps(payload))
    print("HTTP Status:", r.status_code)
    print("JSON: ", r.json())
    return r.json()


if __name__ == '__main__':
    job_json = create_job()

