# create two variables
def atm_machine():
    
User_pin=1122
Balance=20,000
attempts=3
for attempt1 in range(attempts):
    entered_pin=int(input("enter your pin: "))
    if entered_pin == User_pin:
        print("proceed")
        break   
    else:
        print("incorrect pin")
    if attempts == attempts - 1:
        print("too many attempts. card blocked")

atm_machine()
    


      
           
