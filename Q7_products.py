from datetime import MAXYEAR
import mysql.connector

group_number="14" #FILL IN YOUR GROUP NUMBER
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht22_1_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht22_1_project_group_"+group_number
)

# Input
print("Choose product: ")
product = input()
print()

mycursor = mydb.cursor()

# Return product and discount
mycursor.execute("SELECT Prod_title, Discount FROM Product WHERE Prod_title ='" + product + "'")
myresult = mycursor.fetchall()

# Check if product exists
if myresult != []:
  # Print current discount, take input for new discount
  print("Product: " + product, "\t Current discount: " + str(myresult[0][1]))
  print("Input new discount: ")
  new_discount = input()
  # Set new discount
  mycursor.execute("UPDATE Product SET Discount=" + new_discount + " WHERE Prod_title ='" + product + "'")
else:
  print("Product not found")


mydb.commit()
mydb.close()
