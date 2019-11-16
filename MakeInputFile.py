import DBHelper

if __name__ == "__main__":
    f = open("NotEvil.txt", 'w',encoding="utf-8")
    f2 = open("Evil.txt", 'w',encoding="utf-8")
    f3 = open("NotAbuse.txt", 'w',encoding="utf-8")
    f4 = open("Abuse.txt", 'w',encoding="utf-8")
    

    for i in DBHelper.GetDB(None):
        if 'evil' not in i.keys():
            pass
        elif i['evil']=="0":
            #f.write(i["_id"]["$oid"]+" "+i['text']+'\n')
            f.write(i['text']+'\n')
        elif i['evil']=="1":
            #f2.write(i["_id"]["$oid"]+" "+i['text']+'\n')
            f2.write(i['text']+'\n')
        if 'abuse' not in i.keys():
            pass
        elif i['abuse']=="0":
            f3.write(i['text']+'\n')
        elif i['abuse']=="1":
            f4.write(i['text']+'\n')
    f.close()
    f2.close()
    f3.close()
    f4.close()