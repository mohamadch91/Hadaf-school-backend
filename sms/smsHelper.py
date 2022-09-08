from logging import PlaceHolder
from kavenegar import *
import json
from datetime import datetime, timedelta
import time
def sms_list(start,end):
    # start=datetime.now()
    if(start is not None and start !=''):
        start=datetime.strptime(start, '%Y-%m-%d').date()
        t=int(time.mktime(start.timetuple()))
        print(t)
    if(end is not None and end!=''):
        end=datetime.strptime(end, '%Y-%m-%d').date()
        end=int(time.mktime(end.timetuple()))

    try:
        # t=datetime.now()
        # t=int(time.mktime(t.timetuple()))
        # print(t)
        api = KavenegarAPI("7241662B7842714F6432733071565837556433563863394D3543716E7973346679515745415343386F78453D")
        params = {
            'startdate': t,
            'enddate': end ,
        }   
        response = api.sms_selectoutbox(params)
        return response
    except APIException as e: 
        print (str(e))
    except HTTPException as e: 
        print (str(e))

def last_sends():
    try:
        api = KavenegarAPI("7241662B7842714F6432733071565837556433563863394D3543716E7973346679515745415343386F78453D")
        params = {
            'Long': 100,
        }   
        response = api.sms_latestoutbox(params)
        return response
    except APIException as e: 
        print (str(e))
    except HTTPException as e: 
        print (str(e))        

def send_bulk(phones,message):
    try:
       
        ans=''
        for i in phones:
            ans+=i+','
        api = KavenegarAPI("7241662B7842714F6432733071565837556433563863394D3543716E7973346679515745415343386F78453D")
        params = {
            'sender': '0018018949161',
            'receptor': ans,
            'message': message,
        }   
        response = api.sms_send(params)
        return response
    except APIException as e: 
        print (str(e))
    except HTTPException as e: 
        print (str(e))