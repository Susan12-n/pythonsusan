# nhif premium rates 
salary =float(input("please enter your salary : ").lower())
if salary <=0:
  print("invalid amount")
elif salary <= 5900:
  print("150.00")
elif salary <=7999:
  print("300.00")
elif salary<=11999:
  print("400.00")
elif salary<=14999:
  print("500.00")
elif salary<=19999:
  print("600.00")
elif salary<=24999:
  print("750.00")
elif salary<=29999:
  print("850.00")
elif salary<=49999:
  print("1000.00")
elif salary<=99999:
  print("1500.00")
else:
  print("2000.00")

