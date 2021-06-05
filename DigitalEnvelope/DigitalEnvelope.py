# BIRBAL BHUTRA
# ID - 510517013

# Digital Envelope program

# RSA Algorithm has been used here to create the digital envelope


# uuid is used to generate random unique ID 
import uuid
# hashlib is a python package/library to do hashing
import hashlib
# Caesar Cipher is a way to do encryption
from caesarcipher import CaesarCipher

# Utility function to calculate gcd 
def gcd(a,b):
    while(b):
        a, b = b, (a % b)
    return a

# Utility function to calculate modulo inverse
def moduloInverse(a,b):
    a = a % b
    for i in range(1,b):
        if ((a*i) % b) == 1:
            return i

# Utility function to perform hashing
def hashing(word):
    salt = uuid.uuid4().hex
    encode = salt.encode() + word.encode()
    hashedValue = hashlib.sha256(encode).hexdigest() + ':' + salt
    return hashedValue

# Utility function to compare hash values
def hashComparison(hashedMessage,newMessage):
    password, salt = hashedMessage.split(':')
    encode = salt.encode() + newMessage.encode()
    if password == hashlib.sha256(encode).hexdigest():
        return True
    else:
        return False

# Function to input data
def inputPrimeNumbers():
    firstPrimeNumber = int(input("Enter the value of first prime number: "))
    secondPrimeNumber = int(input("Enter the value of second prime number: "))
    # If firstPrimeNumber and secondPrimeNumber are equal
    if firstPrimeNumber == secondPrimeNumber:
        print("Inavlid ---> Value of both prime numbers are same.")
        inputPrimeNumbers()
        exit()
    # Public key should be accessible by all.
    publicKey = int(input("Enter the PUBLIC KEY: "))
    print("\nLoading! Please Wait.")
    return firstPrimeNumber,secondPrimeNumber,publicKey

# Utility function to generate keys
def generateKey(firstPrimeNumber,secondPrimeNumber):
    n = firstPrimeNumber * secondPrimeNumber
    totientFunction = (firstPrimeNumber-1)*(secondPrimeNumber-1)

    temp = 1
    while(temp):
        e = int(input("Enter value of e: "))
        if gcd(totientFunction,e) != 1:
            print("\nGCD should be relatively prime.")
            print("\nEnter value again!")
            continue
        temp = 0

    if e>1 and e<totientFunction:
        d = moduloInverse(e,totientFunction)
        print("\nWith respect to RSA algorithm d is: %s" %(d))

    print("\nPublic Key is - PU(%s,%s)" %(e,n))
    print("Private Key is - PR(%s,%s)" %(d,n))
    return n,e,d

# Utility function for key encryption
def encryptionProcess(e,n,publicKey):
    Cipher = (publicKey**e) % n
    print("\nCipher text generated is: %s" %(Cipher))
    return Cipher

# Utility function for message encryption
def messageEncryption(publicKey):
    messages = input("\nEnter the message: ")
    hashedMessage = hashing(messages)
    print("\nHash for the given message is: %s" %(hashedMessage))

    cipher = CaesarCipher(messages, offset= publicKey)
    encryptedMessage = cipher.encoded
    print("Encrypted message is: %s" %(encryptedMessage))
    return hashedMessage, encryptedMessage

# Utiltiy function for key decryption
def decryptionProcess(n,d,Cipher,publicKey):
    Decipher = (Cipher**d) % n
    print("\nDecrypted public key is %s" %(Decipher))
    print("\nThis match with original public key - %s" %(publicKey))
    return Decipher

# Utility function for message decryption
def messageDecryption(hashedMessage,encryptedMessage,Decipher):
    decipher = CaesarCipher(encryptedMessage, offset= Decipher)
    decryptedMessage = decipher.decoded
    print("\nDecrypted message is: %s" %(decryptedMessage))
    if hashComparison(hashedMessage,decryptedMessage):
        print("\n--> The hashes are same.")
    else:
        print("\n-->The hashes are different")


# Driver Code

if __name__ == '__main__':
    while(1):
        print ("Please Select the mode of operation:- \n")
        print ("Press 1 to give your input.")
        print ("Press 2 to generate key.")
        print ("Press 3 to perform encryption using RSA algorithm.")
        print ("Press 4 to perform symmetric encryption.")
        print ("Press 5 to perform decryption for the public key.")
        print ("Press 6 to perform decryption of the message.")
        print ("Press 7 to Quit.\n")
        choice = int(input("Press the required key: "))
        print("\n")
        if choice == 1:
            p,q,publicKey = inputPrimeNumbers()
        elif choice == 2:
            n,e,d = generateKey(p,q)
        elif choice == 3:
            Cipher = encryptionProcess(e,n,publicKey)
        elif choice == 4:
            hashedMessage,encryptedMessage = messageEncryption(publicKey)
        elif choice == 5:
            Decipher = decryptionProcess(n,d,Cipher,publicKey)
        elif choice == 6:
            messageDecryption(hashedMessage,encryptedMessage,Decipher)
        elif choice == 7:
            break
        else:
            print("Invaid Input!")
