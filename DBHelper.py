import requests
import json
import argparse

#URL = 'http://15.165.19.243:5000/' 
URL = 'http://10.255.55.43:5000/' 

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


if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description='input startPage, endPage')
    #parser.add_argument('id', type=str,
    #                help='id')
    #parser.add_argument('data', type=int,
    #                help='data')
    #args = parser.parse_args()
    #data={'evil':args.data}
    #UpdateDB(args.id,data)
    deleteList = ["5dcbf981c438f2035e633dcb","5dcbf987c438f2035e633de2","5dcbf9b2c438f2035e633ea5", "5dcbfa23c438f2035e633f33","5dcbfa48c438f2035e633feb","5dcbfa59c438f2035e634027","5dcbfa94c438f2035e6340ab","5dcbfcb1c438f2035e6346bf","5dcbfcb1c438f2035e6346c7"]

    for delete in deleteList:
        data={'evil':4}
        UpdateDB(delete,data)