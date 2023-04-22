print("------------------TOLLGATE REGISTER SYSTEM-------------------")
print("-------------------------------------------------------------")
print("\n\n")
data={}
wallet=0
c=int(input("press 1 to conitnue...... : "))
while(c==1):
    print("1...REGISTRATION \n2..DRIVER")
    ch=int(input("enter your choice : "))
    if(ch==1):
        print("---------welcome admin-----------")
        print("\n\n")
        vno="vehicle_number"
        na="owner_name"
        ma="make"
        ye="year"
        bill="balance"
        rc="RC"
        no=input("enter vehicle number :  ")
        data[vno]=no
        data[na]=input("enter the customer name :")
        data[ma]=input("enter the make name  :")
        data[ye]=int(input("enter the year : "))
        data[rc]=input("enter the RC number : ")
        bill1=int(input("Recharge your wallet :  "))
        wallet=wallet+bill1
        data[bill]=wallet
        print("your payment successfull...!!!!!")
        print("********************************")
        print("Thank you ... Enjoy your  journey!!!!!")
    elif(ch==2):
        print("--------------------------------------------------------")
        name=input("enter the customer name :")
        inu=input("enter the RC number : ")
        if(inu==data[rc] and name==data[na]):
            print("login successfull............")
            print("-----------------------------------------")
            print("--------------CUSTOMER DETAILS-----------")
            print("-----------------------------------------")
            print("RC NUMBER      : ",data[rc])
            print("VEHICLE_NAME   : ",data[ma])
            print("VEHICLE_NUMBER : ",data[vno])
            print("CUSTOMER_NAME  : ",data[na])
            print("YOUR_WALLER    : ",data[bill])
            print("------------------------------------------")
            print("------------------------------------------")
            if(data[bill]<550):
                print("INSUFFIENT BALANCE.....")
            else:
                reduc=data[bill]
                red=reduc-50
                data[bill]=red
                print("your payment is successfull........!!! ")
                print("---------------------------------------")
                print("your wallet balance  :           " ,red)
                print("---------------------------------------")
                print("Thank you....Happy journey......")
        else:
            print("INVALID DATA......")
            break
    else:
        print("INVALID CHOICE....")
    ca=int(input("press 0 to exit and 1 to continue...... :"))         
    if(ca==0):
        break

    