from kavenegar import *
import json
def send_otp(otp):
    print("otp password")
    print(otp.password)
    try:
        api = KavenegarAPI("7241662B7842714F6432733071565837556433563863394D3543716E7973346679515745415343386F78453D")
        params = {
            'sender': '2000500666',
            'receptor': otp.receiver,
            'message': 'test message to user '
        }   
        response = api.sms_send(params)
        print (response)
    except APIException as e: 
        print (str(e))
    except HTTPException as e: 
        print (str(e))