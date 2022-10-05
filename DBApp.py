import mysql.connector

group_number="14" #FILL IN YOUR GROUP NUMBER
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht22_1_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht22_1_project_group_"+group_number
)

# Input
print("Input Department name: ")
dep = input()
print()

mycursor = mydb.cursor()

# Return all child departments 
mycursor.execute("SELECT Dep_title FROM Department WHERE Parent_title ='" + dep + "'")
myresult = mycursor.fetchall()

if len(myresult) == 0: # If leaf, print related products
  mycursor.execute("select Prod_title, Description, Price from ( SELECT Reviews.Prod_title, Description, Price, VAT, Discount, avg(Stars) as avg_rating FROM Product inner join Reviews on Reviews.Prod_title = Product.Prod_title Group by Prod_title ) as T1 where Prod_title in (select HP_Prod_title from HasProducts where HP_Dep_title='" + dep +"');")

  myresult = mycursor.fetchall()
  print("Products related to department: " + dep)
  for x in myresult:
    print(str(x[0]) + "\t" + str(x[1]) + "\t" + str(x[2]))
  
else: # Not leaf, print child departments 
  print("Child departments of " + dep + ":")
  for row in myresult:
    print(row[0])

mydb.close()