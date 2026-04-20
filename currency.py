def usd(pkr):
    print(f"Here is your Currency in USD {pkr*0.0036}")

def dinar(pkr):
    print(f"Here is your Currency in Dinar {pkr*0.0011}")
    
def riyal(pkr):
    print(f"Here is your Currency in Riyal {pkr*0.013}")
    
def dirham(pkr):
    print(f"Here is your Currency in Dirham {pkr*0.013}")
        
def pound(pkr):
        print(f"Here is your Currency in POUND{pkr*0.0027}")
    
print("Welcome to currency exchange")

count=int(input("Which country you want your pkr to be exchanged? : \n1.PKR to USD \n2.PKR to Dinar \n3.PKR to RIYAL \n4.PKR to DIRHAM \n5.PKR to POUND"))
curr=eval(input(f"Enter an Amount you want to convert from pkr:"))
if count==1:
    usd(curr)
elif count==2:
    dinar(curr)
elif count==3:
    riyal(curr)
elif count==4:
    dirham(curr)
elif count==5:
    pound(curr)
else:
    print("Invalid")
        