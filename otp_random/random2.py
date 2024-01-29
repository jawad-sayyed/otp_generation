import random
otp=(random.randint(1000,9999))
print(f'Your otp is : {otp}')

import random  #otp generation using logic building
otp_again="yes"
while otp_again=="yes":
    output=""
    for i in range(0,4):
        output=output+str(random.randint(0,9))
    print(output)
    otp_again=input("do you want to resent otp? :")
   



#otp using function
import random
def otp():
    otp_again="y"
    while otp_again=="y":
        output=""
        for i in range(0,4):
            output=output+str(random.randint(0,9))
        print(output)
        otp_again=input("do you want to resent otp? :")

otp()