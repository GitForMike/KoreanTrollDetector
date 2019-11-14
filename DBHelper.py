import requests
import json

URL = 'http://15.165.19.243:5000/' 

def UpdateDB(ID,data):
    updateURL = URL+"reply/"+ID
    headers={"Content-Type": "application/json"}
    print(updateURL)
    print(data)
    response = requests.post(updateURL,headers=headers,data=json.dumps(data))
    if response.status_code!=200:
        print(response.status_code)
        print(response.text)
        exit(1)
    print(response.text)

def GetDB(startPage=None,endPage=None):
    if startPage==None or endPage==None:
        response = requests.get(URL)
        if response.status_code!=200:
            print(response.text)
            exit(1)
        return response.json()

    result = []
    for i in range(startPage,endPage):
        response = requests.get(URL+'table/'+str(i)) 
        if response.status_code!=200:
            print(response.text)
            exit(1)
        result += response.json()
    return result