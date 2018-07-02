import requests as rq
import json
from tkinter import askopenfilename
import boto3
import os

#zencoder contract:
key, url = str(os.environ['ZENKEY']), "https://app.zencoder.com/api/v2/jobs/"
#ask user a file to upload
video = askopenfilename()


def create_job(url=url, key=key, headers=
               {"Zencoder-Api-Key": key, "Content-Type": "application/json"},
               payload={
                  "test": "true",
                  "input": "s3://zencodertesting/test.mov",
                  "outputs": [
                                {
                                    "label": "mp4 high",
                                    "url": "s3://learning-services-media.brightcove.com/\
                                    output-file-name.mp4",
                                    "h264_profile": "high"
                                    }]}):
    '''This method creates a JOB on Zencoder API and sets the output converted
    file.'''
    sts = rq.get(url, headers=headers)
    print(sts)
    r = rq.post(url, headers=headers, data=json.dumps(payload))
    print("HTTP Status:", r.status_code)
    print("JSON: ", r.json())
    return r.json()


def list_jobs(headers={"Zencoder-Api-Key": key, "Content-Type": "application/json"}):
    '''This method lists all created jobs on Zencoder API.'''
    l = rq.get(url+"?"+key, headers=headers)
    print(l.json())
    return(l)


def upload_video(video):
    '''This method uploads the input video to Amazon AWS S3 Server.'''
    s3 = boto3.resource('s3')
    with open(video, 'rb') as vd:
        s3.bucket(my_bucket).put_object(key=video, Body=vd)



if __name__ == '__main__':
#    job_json = create_job()
    list_jobs()
