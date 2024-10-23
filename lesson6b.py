# if...elif....else statements 
# used yto execute a block of statement with alternative ,which can be more than two 
# days of the week 
day=input("please enter the day of the week : ").lower()
if day=="monday":
    print("it on a monday")
if day=="tuesday":
    print("it on a tuesday")
elif day=="wednesday":
    print("it on a wednesday")
elif day=="thursday":
    print("it on a thursday")
elif day=="friday":
    print("it on a friday")
elif day=="saturday":
    print("it on a saturday")
elif day=="sunday":
    print("it on a sunday")
else:
    print("invalid day of the week")


# checking for counties 
county=input("please enter your county : ").lower()
if county=="mombasa":
    print("this is mombasa county")
elif county=="nakuru":
    print("nakuru")
elif county=="kericho":
    print("kericho")
elif county=="kisumu":
    print("kisumu")
elif county=="nandi":
    print("nandi")
elif county=="muranga":
    print("muranga")
elif county=="njeri":
    print("nyeri")
elif county=="lamu":
    print("lamu")
elif county=="turkana":
    print("turkana")
elif county=="isiolo":
    print("isiolo")
else :("invalid county")

