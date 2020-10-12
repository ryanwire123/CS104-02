#must initialize inpt as int to concatenate with intgers in 'if statement'
temp = int(input ("Please enter the current temp: "))
while (temp != 999):
    if (temp > 90):
        print("Wear shorts")
        temp = int(input("Please enter the current temp: "))
    elif (temp > 70):
        print("Short sleeves are fine")
        temp = int(input("Please enter the current temp: "))
    elif (temp > 50):
        print("Wear a jacket")
        temp = int(input("Please enter the current temp: "))
    elif (temp > 32):
        print("Wear a heavy coat")
        temp = int(input("Please enter the current temp: "))
    else:
        print ("Stay inside")
        temp = int(input("Please enter the current temp: "))
    if (temp == 999):
        break
