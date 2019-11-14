import DBHelper

if __name__ == "__main__":
    for i in DBHelper.GetDB(None):
        if 'abuse' in i.keys():
            continue
        print(i['text'])
        while True:
            stdin = input("good 0, bad 1, skip 2, exit 3: ")
            if stdin =="3":
                exit(0)
            elif stdin =="1":
                data={'abuse':'1'}
                DBHelper.UpdateDB(i['_id']['$oid'],data)
                break
            elif stdin =="0":
                data={'abuse':'0'}
                DBHelper.UpdateDB(i['_id']['$oid'],data)
                break
            elif stdin =="2":
                print("skip")
                break