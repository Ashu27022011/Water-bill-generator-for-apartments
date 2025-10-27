

print("Enter the flat numbers separated by commas:")
a = input("").split(",")

print("Enter the beginning readings separated by commas:")
b = input("").split(",")
import database as db
beginning_reading = {u : int(v) for u,v in zip(a,b)}

db.beginning_readings = beginning_reading

print(db.beginning_readings)