import requests
import json 
import os

def send_sms(number,message):
    url ="https://www.fast2sms.com/dev/bulk"
    params ={
       "authorization":"D3or7Xiet1zxNpZnCKj2hEHTyIJFdP8VWlGSs4cUq9bkwmA0gfdOXfZo2Ri7wqnhxWVDur1sp6eFblG4",
       "sender_id" :"FSTSMS",
       "message":message,
       "language":"english",
       "route":"p",
       "numbers":number
    }

    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)


send_sms("type here your number","hello how are you")