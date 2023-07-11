from kavenegar import *
import json
def send_otp(otp):
    print("otp password")
    print(otp.password)
    try:
        api = KavenegarAPI("38395854544B596663304931486958384B454168554568446F4D4D4374344F2F446F71362B5A55694B33453D")
        params = {
            'sender': '0018018949161',
            'receptor': otp.receiver,
             'template': 'OTP',
            'token': otp.password,
            'type': 'sms'
        }   
        response = api.verify_lookup(params)
    except APIException as e: 
        print (str(e))
    except HTTPException as e: 
        print (str(e))