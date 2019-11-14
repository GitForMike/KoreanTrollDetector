import DBHelper
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='input startPage, endPage')
    parser.add_argument('--startPage', type=int,
                    help='input start page')
    parser.add_argument('--endPage', type=int,
                    help='input start page')
    args = parser.parse_args()

    for i in DBHelper.GetDB(args.startPage,args.endPage):
        if 'evil' in i.keys():
            continue
        print(i['text'])
        while True:
            stdin = input("good 0, bad 1, skip 2, exit 3: ")
            if stdin =="3":
                exit(0)
            elif stdin =="1":
                data={'evil':'1'}
                DBHelper.UpdateDB(i['_id']['$oid'],data)
                break
            elif stdin =="0":
                data={'evil':'0'}
                DBHelper.UpdateDB(i['_id']['$oid'],data)
                break
            elif stdin =="2":
                print("skip")
                break