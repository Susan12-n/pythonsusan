# functions with parameters 
def car_display(car):
    print("I am seeing that car",car)
def askHisName(name):
    print("He says his name is",name)
def askHisNumber(Number):
    print("the number is",Number)
def askQuestions(status,address):
    print("His status and address is",status,address)
def requestHim(visit,chocolate,dinner):
    print("the response is",visit,chocolate,dinner)
def haveDinner(eat,watch_movie):
    print("have dinner and wath movie",eat,watch_movie)


#fuction to add two numbers
def addnumbers(number1,number2):
    sum=number1+number2
    print("the sum is",sum)
     
# 3substract two numbers
def sub(number1,number2) :
    sub=number1-number2
    print("the result is",sub)
#multiplication
def mult(number1,number2,number3) :
    mult=number1*number2*number3
    print("the product is",mult)
#division
def result(number1,number2) :
    result=number1/number2
    print("the result is",result)

# area of a circle 
def area(rad,pie):
    area=pie*rad*2
    print("the area of the circle is",area)

#simple interest

def interest(p,r,t):
    interest=p*r*t/100
    print("the simple interest is",interest)
# Bmi
def my_bmi(weight,height):
    bmi=weight/height*height
    print("my bmi is",bmi)

if __name__=="__main__":
   addnumbers(13,12)
   mult(30,6,4)
   result(30,6)
   area(12,3.14)
   interest(1000,28,2)
   haveDinner("eat","dinner")
   requestHim("visit","accept chocolate","go dinner")
   askQuestions("single","kisumu")
   askHisNumber("0712461219")
   askHisName("Ken")
   my_bmi(65,1.9)

   
   
   


 
   


