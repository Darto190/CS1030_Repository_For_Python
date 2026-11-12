validAccsesCardPin = 1234
validUserPin = 0000

accsesCardPin = int(input("Tap your id card:"))
if validAccsesCardPin == accsesCardPin:
    userPin = int(input("Enter your user PIN:"))
    if validUserPin == userPin:
        print ("welcome")
    elif userPin >=9999:
        print ("invaled user pin pin must be 4 digits")
    elif userPin <=1000:
                print ("invaled user pin pin must be 4 digits")
    elif userPin != validUserPin:
        print ("invaled user pin")
    else:
        print ("invaled")
else:
    print("invaled card")