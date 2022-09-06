
SECRET_KEY='vUBbw45VhCsDlw0djlSAtBxaM7HMhko2VlaxNIE1BI8'
FIX_URL='https://live.iranbama.com/bigbluebutton/api/'
from django.contrib.auth.hashers import make_password
import hashlib
import requests
import xml.etree.ElementTree as ET
import json, xmljson
from lxml.etree import fromstring, tostring

def create(name,id):
    id=str(id+10)
    create_query='allowStartStopRecording=false&attendeePW=hadaf&autoStartRecording=true&meetingID='+id+'&moderatorPW=hadaf&name='+name+'&record=true&voiceBridge=76572&welcome=welcome'
    string='create'+create_query+SECRET_KEY
    result = hashlib.sha1(string.encode())
    checksum=result.hexdigest()
    url=FIX_URL+'create?'+create_query+'&checksum='+checksum
    response = requests.get(url)
    xml = fromstring(response.text)
    ans=json.dumps(xmljson.badgerfish.data(xml))
    return ans

def join(name,id):
    id=str(id+10)
    join_query='fullName='+name+'&meetingID='+id+'&password=hadaf&redirect=true'
    string='join'+join_query+SECRET_KEY
    result = hashlib.sha1(string.encode())
    checksum=result.hexdigest()
    url=FIX_URL+'join?'+join_query+'&checksum='+checksum
    return url

def student_join(name,id):
    id=str(id+10)
    join_query='fullName='+name+'&meetingID='+id+'&password=hadaf&redirect=true'
    string='join'+join_query+SECRET_KEY
    result = hashlib.sha1(string.encode())
    checksum=result.hexdigest()
    url=FIX_URL+'join?'+join_query+'&checksum='+checksum
    return url