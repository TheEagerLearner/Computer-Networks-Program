def lrc():

    call=True
    while call:
        bits=str(input("Enter the binary number whose length shuld be in multiples of 8: "))
        if len(bits)%8==0 and len(bits)!=0:
            call=False
        else:
            print("Please enter the number again")
    
    n=len(bits)
    par=str(input("What type of parity is required E for Even and O for Odd : "))
    lst=[]
    
    if(n==8):
        for k in range(4):
            lst.append(0)

        for i in range(4):
            lst[i]=0
            for j in range(i,n,4):
                  lst[i]=int(bits[j])+lst[i]
    else:
        for k in range(8):
            lst.append(0)
        
        for i in range(8):
            lst[i]=0
            for j in range(i,n,8):
                lst[i]=int(bits[j])+lst[i]
    if(par=='o' or par=='O'):
        for i in lst:
            if(i%2!=0):
                bits=bits+str(0)
            else:
                bits=bits+str(1)
    else:
        for i in lst:
            if(i%2!=0):
                bits=bits+str(1)
            else:
                bits=bits+str(0)
    print(bits)


def vrc():
    call=True
    while call:
        bits=str(input("Enter the binary number whose length shuld be in multiples of 8: "))
        if len(bits)%8==0 and len(bits)!=0:
            call=False
        else:
            print("Please enter the number again")
    
    n=len(bits)
    store=[]
    for i in bits:
        store.append(int(i))
    par=str(input("What type of parity is required E for Even and O for Odd : "))
    lst=[]

    if(n==8):
        for k in range(2):
            lst.append(0)
        m=4
        p=0
        a=0
        while(m<=8):
            lst[a]=sum(store[p:m])
            a=a+1
            p=p+4
            m=m+4
        print(lst)
            
    else:
        m=8
        p=0
        a=0
        while(m<=n):
            lst.append(sum(store[p:m]))
            a=a+1
            p=p+8
            m=m+8
        print(lst)
    if(par=='o' or par=='O'):
        for i in lst:
            if(i%2!=0):
                bits=bits+str(0)
            else:
                bits=bits+str(1)
    else:
        for i in lst:
            if(i%2!=0):
                bits=bits+str(1)
            else:
                bits=bits+str(0)
    print(bits)

    
def checksum():
    segsize=int(input("Enter the segment size : "))
    bits=str(input("Enter the binary number whose length should be in multiples of segment size : "))
    call=True
    while(call):
        if(len(bits)%segsize!=0 and len(bits)==0):
            print("Length of the binary number is not in multiples of the segment size")
        else:
            call=False
    lst1=[]
    lst2=[]
    m=0
    p=segsize

    while(p<=len(bits)):
        for i in range(m,p):
            lst2.append(int(bits[i]))
        lst1.append(lst2)
        m=m+segsize
        p=p+segsize
        lst2=[]
    a=0
    lst=[]
    complem=[]

    while(a<len(lst1)):
        val=""
        for i in lst1[a]:
            val=val+str(i)
        lst.append(val)
        a=a+1
    
    sum=""
    a=""
    for i in range(segsize):
        sum=sum+"0"

    for i in lst:
        sum=bin(int(sum,2)+int(i,2))
        if(len(sum[2:])>segsize):
            for j in sum[3:]:
                complem.append(j)
            sum=""
            for k in complem:
                sum=sum+k
            for l in range(segsize-1):
                a=a+"0"
            a=a+"1"
            sum=bin(int(sum,2)+int(a,2))
        else:
            continue
    if(len(sum[2:])<8):
        for i in range(8-len(sum[2:])):
            sum[2:]="0"+str(sum[2:])
    print(sum[2:])



checksum()

