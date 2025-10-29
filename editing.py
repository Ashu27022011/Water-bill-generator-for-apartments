import database as db

print(f"If you want to edit the balance amounts,begging amount and ending amount\n.")
print(db.beginning_readings,"\n",db.ending_readings,"\n",db.balance)

edit_choice = input("Which one do you want to edit? (balance/beginning/ending): ").lower()

if edit_choice == "balance":
    flat,sum = input("Enter the flat number whose balance you want to edit: like G1 : 12 ").split(":") 
    db.balance[flat.lower()] = int(sum)

elif edit_choice == "beginning":
    flat,sum = input("Enter the flat number whose beginning reading you want to edit: like G1 : 12 ").split(":") 
    db.beginning_readings[flat.lower()] = int(sum)

elif edit_choice == "ending":
    flat,sum = input("Enter the flat number whose ending reading you want to edit: like G1 : 12 ").split(":") 
    db.ending_readings[flat.lower()] = int(sum)

else:
    print("Invalid choice.restart from the first.")