validAccsesCardPin = 1234
validUserPin = 0000

accsesCardPin = int(input("Tap your id card:"))
if validAccsesCardPin == accsesCardPin:
    print("valid user card")
    userPin = int(input("Enter your user PIN:"))

    if validUserPin == userPin:
        print ("welcome")
    else:
        print("invalid user pin")
else:
    print("invaled card")