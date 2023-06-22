import random, string
alpha = list(string.ascii_letters)
num = list(string.digits)
sym = ['!','~','@','#','$','%','^','&','*','(',')','{','}','[',']','<','>','?','-','_','=','+','\\','|','/']
password = []
print("\n-----MAY YOUR LIFE BE AN OPEN BOOK BUT YOUR FILES MUST NOT LEFT OPEN-----\n\n")
a,n,s = [int(x) for x in input("Enter number of alphabets, numbers and symbols you want in your password: ").split()]
for i in range(a):
    Alp = random.choice(alpha)
    password += Alp
for i in range(n):
    Numb = random.choice(num)
    password += Numb
for i in range(s):
    Symb = random.choice(sym)
    password += Symb
random.shuffle(password)
pw = ""
for ch in password:
    pw += ch
print(f"\nHere's your password : {pw}")


#It's mine...


symbols = list(string.printable)
a = int(input("\n\nHow many symbols do you want in your password : "))
password = []
for i in range(a):
    Symb = random.choice(symbols)
    password += Symb
random.shuffle(password)
pw = ""
for ch in password:
    pw += ch
print(f"\nHere's your password : {pw}")