import random
from Euclid import euclidsGCD_Func 

import cryptography # testing
from cryptography.fernet import Fernet # testing


# testing crypto functionalities

# generate a key 
key = Fernet.generate_key() 

# write key to file 
file = open('key.key','wb')
file.write(key) # this key is type bytes
file.close()

# read key from the key file 
file2 = open('key.key','rb')
key = file2.read()
file.close()
print(">> The key being used: ",key)

# encode the message 
message = "my deep dark secret."
encoded = message.encode()

# encrypt the message 
f = Fernet(key)
encrypted = f.encrypt(encoded)
print(">> Here is the encrypted message: ", encrypted)

# now to try and decrypt..... too long on standard machine i think, we need quantum power!!


# fint esting of crypto 




















































""""
# def main():
#   print("insert thing here\n");

# if__name__=="__main__":
#   main()



print("CMPE 130 project FA21")

def greeting():
  print("Hello World")
  

greeting() #this prints "Hello World"

a = 10 
b = 15.28374 #as an integer, this automatically converts to just 15. bummer. same goes for "int" in C++
def mult(a,b):
  print(int(a * b))
#so by calling this int function we can convert any numerical data type to type int as needed 

mult(a,b) #this prints the product of a and b, only in integer form(at)

#so sawy we want a default value for a parameter then we can do the following in the function declaration 
def personalGreet(name='Steven'):
  print("hello "+ name)

personalGreet()
#since no name is passed in as a parameter you can see that its going to display the default string of steven, but if we do pass, say richard 
personalGreet("richard")
# we get hello richard B) 

#example while loop 
counter = 0
while counter < 5 :
  counter += 1
  print("counting")

# example for-in loop
list = [1,2,3,4,5]
for numbers in list:
  print(numbers)

#class exampel
class dog: 
  #the below def is the initializer
  def __init__(self, name, age):
    self.name = name
    self.age = age

  #all the rest are just functions using the various properties of the object to be
  def deets(self):
    print(self.name + " is my dog")
  def ageState(self):
    ageStr = str(self.age)
    print("my dog is " + ageStr + " years old.")

myDog = dog('Doug', 12)
myDog.deets()
myDog.ageState()
"""