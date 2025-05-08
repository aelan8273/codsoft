
import random, os

os.system("cls")
x = random.randrange(1111, 9999)

while True:
    print('OTP : ', x)
    try:
        y = int(input("Enter Your OTP: "))
    except ValueError:
        os.system("cls")
        print('Type Only Numbers Not Text:\n')
        continue

    if x == y:
        os.system("cls")
        print("OTP Valid: ✅")
        break
    
    else:
        os.system("cls")
        print("OTP Not Valid: ❌\n")
        continue
    
print("\nWelcome to Website:\n")
