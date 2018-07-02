import requests as rq
import json
from tkinter import askopenfilename, askdirectory
import boto3

key="cef97ec9aa4f0ed89b2c7c128c3bee98"
url = "https://app.zencoder.com/api/v2/jobs/"
video = askopenfilename()


def create_job(url = url, key= key,
              headers = {"Zencoder-Api-Key":key, "Content-Type":"application/json"},
              payload = {"test": "true","input": "s3://zencodertesting/test.mov"}):
    sts = rq.get(url, headers = headers)
    r = rq.post(url, headers = headers, data = json.dumps(payload))
    print("HTTP Status:", r.status_code)
    print("JSON: ", r.json())
    return r.json()

def upload_video(video):
    s3 = boto3.resource('s3')
    with open(video, 'rb') as vd:
        s3.bucket(my-bucket).put_object(key=video, Body=vd)



if __name__ == '__main__':
    job_json = create_job()

