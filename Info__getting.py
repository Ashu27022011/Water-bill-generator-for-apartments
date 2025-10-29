import database as db

apt_name = input("Enter the name of the apartment: ")

# Getting beginning readings from user
print("Enter the flat numbers separated by commas:")
a = input("").lower()
a = a.split(",")
k = list(a)

# Creating a dictionary for beginning readings  
beggred = {}
print("Enter the beginning readings separated by commas:")
for flats in k:
    f = float(input(f"Beginning reading for flat {flats}: "))
    beggred[flats] = int(f)
# Assigning the beginning readings to the database
db.beginning_readings = beggred

# Getting balance amounts from user
balll={}
balaces = input("enter the balance amount if zero enter all zero or no")

#if all values are zero
if balaces.lower() == "all zero":
    balacess = {g : 0 for g in db.beginning_readings.keys()}   
    db.balance = balacess

# if it is not zero  
elif balaces.lower() == "no":
    for bal in k:
        balance = float(input(f"Enter balance for flat {bal}: "))
        balll[bal] = int(balance)
    db.balance = balll
    # Assigning the balance amounts to the database

#else something is wrong
else:
    print("Invalid input for balance. Please enter 'all zero' or 'no'.")

#signify successful saving of data
print("your beginning readings and balance are saved successfully.")    
    
