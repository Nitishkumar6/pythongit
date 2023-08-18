myqueeue=[]
while True:
    if(len(myqueeue)<10):
            data=int(input("enter data"))
            myqueeue.append(data)
            print(myqueeue)
    else:
          data=int(input("enter data"))
          myqueeue.remove(myqueeue[0])
          myqueeue.append(data)
          print(myqueeue)