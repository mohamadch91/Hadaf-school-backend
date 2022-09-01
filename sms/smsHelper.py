from kavenegar import *
import json
from datetime import datetime, timedelta
from datetime import datetime, timedelta
import time
def sms_list():
    print("otp password")
    start=datetime.now()
    t=int(time.mktime(start.timetuple()))
    try:
        api = KavenegarAPI("7241662B7842714F6432733071565837556433563863394D3543716E7973346679515745415343386F78453D")
        params = {
            'startdate': 1661314178,
            'enddate': '' ,
        }   
        response = api.sms_selectoutbox(params)
        return response
    except APIException as e: 
        print (str(e))
    except HTTPException as e: 
        print (str(e))