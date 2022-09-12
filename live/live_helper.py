
SECRET_KEY='vUBbw45VhCsDlw0djlSAtBxaM7HMhko2VlaxNIE1BI8'
FIX_URL='https://class.srvschool.ir/bigbluebutton/api/'
from django.contrib.auth.hashers import make_password
import hashlib
import requests
import xml.etree.ElementTree as ET
import json, xmljson
from lxml.etree import fromstring, tostring
import urllib.parse
def create(name,id):
    welcome='به کلاس'+name+'خوش آمدید'
    welcome=urllib.parse.quote(welcome)
    name=urllib.parse.quote(name)
    voice_bridge=str(id+10000)
    id=str(id+10)

    create_query='allowStartStopRecording=true&attendeePW=hadafuser&autoStartRecording=false&meetingID='+id+'&moderatorPW=hadafadmin&name='+name+'&record=true&voiceBridge='+voice_bridge+'&welcome=+'+welcome
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
    name=name.split(" ")
    name1=name[0]
    name2=name[1]
    name1=urllib.parse.quote(name1)
    name2=urllib.parse.quote(name2)
    join_query='fullName='+name1+'+'+name2+'&meetingID='+id+'&password=hadafadmin&redirect=true'
    string='join'+join_query+SECRET_KEY
    result = hashlib.sha1(string.encode())
    checksum=result.hexdigest()
    url=FIX_URL+'join?'+join_query+'&checksum='+checksum
    return url

def student_join(name,id):
    id=str(id+10)
    name=name.split(" ")
    name1=name[0]
    name2=name[1]
    name1=urllib.parse.quote(name1)
    name2=urllib.parse.quote(name2)
    join_query='fullName='+name1+'+'+name2+'&meetingID='+id+'&password=hadafadmin&redirect=true'

    string='join'+join_query+SECRET_KEY
    result = hashlib.sha1(string.encode())
    checksum=result.hexdigest()
    url=FIX_URL+'join?'+join_query+'&checksum='+checksum
    return url 

def getmeetings():
    string='getMeetings'+SECRET_KEY
    result = hashlib.sha1(string.encode())
    checksum=result.hexdigest()
    url=FIX_URL+'getMeetings?'+'&checksum='+checksum
    response = requests.get(url)
    xml = fromstring(response.text)
    ans=json.dumps(xmljson.badgerfish.data(xml))
    ans=ans.replace("$:","").replace(" ","").replace("k",'')
    ans=json.loads(ans)
    data=[]
    ans=ans["response"]
    if(type(ans["meetings"]["meeting"]) is list):
        for i in ans["meetings"]["meeting"]:
            print(i)
            new_data={}
            new_data["name"]=i["meetingName"]["$"]
            new_data["id"]=i["meetingID"]["$"]-10
            new_data["url"]=join("main admin",i["meetingID"]["$"]-10)
            data.append(new_data)              
    elif(type(ans["meetings"]["meeting"]) is dict):
        i=ans["meetings"]["meeting"]
        new_data={}
        new_data["name"]=i["meetingName"]["$"]
        new_data["id"]=i["meetingID"]["$"]-10
        # print(getpastmeeting(i["meetingID"]["$"]-10))
        new_data["url"]=join("main admin",i["meetingID"]["$"]-10)
        data.append(new_data)
    return data

def end(id):
    id=str(id+10)
    end_query='meetingID='+id+'&password=hadafadmin'
    string='end'+end_query+SECRET_KEY
    result = hashlib.sha1(string.encode())
    checksum=result.hexdigest()
    url=FIX_URL+'end?'+end_query+'&checksum='+checksum
    response = requests.get(url)
    xml = fromstring(response.text)
    ans=json.dumps(xmljson.badgerfish.data(xml))
    return ans

def getpastmeeting(id):
    id=str(id+10)
    id=24
    # end_query='meetingID='+str(id)
    # string='getPastMeetingInfo'+end_query+SECRET_KEY
    # result = hashlib.sha1(string.encode())
    # checksum=result.hexdigest()
    # url=FIX_URL+'getPastMeetingInfo?'+end_query+'&checksum='+checksum
    # response = requests.get(url)
    # xml = fromstring(response.text)
    # ans=json.dumps(xmljson.badgerfish.data(xml))
    # ans=ans.replace("$:","").replace(" ","").replace("k",'')
    # ans=json.loads(ans)
    # data=[]
    # ans=ans["response"]
    # print(ans)
    # print(ans["meetings"])
    # if(len(ans["recordings"])>1):
    #     for i in ans["recordings"]["recording"]:
    #         print(i)
    #         new_data={}
    #         new_data["name"]=i["name"]["$"]
    #         new_data["url"]=i["playback"]["format"][0]["url"]["$"]
    #         data.append(new_data)              
    # elif(len(ans["recordings"])==1):
    #     i=ans["recordings"]["recording"]
    #     new_data={}
    #     new_data["name"]=i["name"]["$"]
    #     new_data["url"]=i["playback"]["format"][0]["url"]["$"]
    #     data.append(new_data)
    # return data