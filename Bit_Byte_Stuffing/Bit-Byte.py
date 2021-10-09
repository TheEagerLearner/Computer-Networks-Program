def byte():
    final=['F']
    val=input("Enter the input Stream: ")
    for i in range(len(val)):
        if(val[i]=='F'):
            final.append("~F")
        elif(val[i]=="~"):
            final.append("~~")
        else:
            final.append(val[i])
    final.append('F')
    ByteStuffing=""
    for i in final:
        ByteStuffing=ByteStuffing+i
    print("After byte stuffing we get: "+ByteStuffing)
    dbyte(ByteStuffing)
    print("")

def dbyte(val):
    lst=[]
    for i in val:
        lst.append(i)
    lst=lst[1:len(lst)-1]
    ls=[]
    aa=0
    af=0
    pu=""
    for i in lst:
        if(i=="~" and (aa==0 and af==0)):
            aa=aa+1
            af=af+1
        elif(i=="F"):
            af=af+1
        elif(i=="~"):
            aa=aa+1
        else:
            aa=0
            af=0
            ls.append(i)
        if(af==2):
            ls.append("F")
            af=0
            aa=0
        elif(aa==2):
            ls.append("~")
            aa=0
            af=0
    for i in ls:
        pu=pu+i
    print("After byte destuffing we get: "+pu)

        

def bit():
    bits=[]
    bits.append("01111110")
    val=input("Enter the bit stream: ")
    con=0
    bitstuff=""

    for i in val:
        if(con==5):
            if(i=="1"):
                bits.append(0)
            bits.append(i)
            con=0
        elif(i=="1"):
            con=con+1
            bits.append(i)
        else:
            con=0
            bits.append(i)
    bits.append("01111110") 
    for i in bits:
        bitstuff=bitstuff+str(i)
    print("After bit stuffing we get: "+bitstuff)
    dbit(bitstuff)
    print("")

def dbit(val):
    lst=[]
    ls=[]
    for i in val[8:len(val)-8]:
        lst.append(i)
    con=0
    for i in range(len(lst)):
        if(con==5):
            if(lst[i]=="0"):
                if(lst[i+1]=="1"):
                    con=0
                    continue
                else:
                    ls.append(lst[i])
                    con=0
            else:
                con=0
        elif(lst[i]=="1"):
            con=con+1
            ls.append(lst[i])
        else:
            con=0
            ls.append(lst[i])
        pu=""
    for i in ls:
        pu=pu+i
    print("After bit destuffing we get: "+pu)



    


def main():
    choice=int()
    while(True):
        print("Press 1: Byte Stuffing and Destuffing")
        print("Press 2: Bit Stuffing and Destuffing")
        print("Press 3: Exit")
        choice=int(input("Enter Your Choice: "))
        if(choice==1):
            byte()
        elif(choice==2):
            bit()
        elif(choice==3):
            print("Program ended succesfully")
            break
        else:
            print("Please enter a proper input value")
            

main()