import cryptography 

# in here maybe add the class for the cyphered object

class encryptMe:
  def __init__(self, value, private_key, public_key,hash):
    self.value  = value
    self.hash = hash
    self.private_key = private_key
    self.public_key = public_key

  def printHash(self):
    print("Hash is: " + self.hash)
    # i need to review how the hash and keys work consider all of this placeholder stuffs 

cypher1 = encryptMe(0,0,0,0,0)
cypher1.printHash()

