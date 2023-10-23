Speed = float(input("Enter Speed : "))
Miles = 0
if Speed > 200 :
    Miles = 124
else:
    Miles = 100
print ("Your Speed : " +str(Miles))


Bounty = float(input("Enter Bounty : "))
Extra = 0
if Bounty > 3000000:
    Extra = 50000
else:
    Extra = 200
print ("Your Bounty is :" +str(Extra+Bounty))

Bounty = int(input("Enter the bounty that you earned : "))
experience = float (input("How long have you been a bounty hunter? : "))

if Bounty > 500000:
 if experience >=3:
          print ("You are Qualified for the reward")
 else : 
     print ("Sorry but your experience is not qualified")
else:
    print ("You are not able to redeem the bounty")
