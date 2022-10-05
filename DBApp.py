import mysql.connector

group_number="14" #FILL IN YOUR GROUP NUMBER
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht22_1_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht22_1_project_group_"+group_number
)

print("Input Department name: ")
dep = input()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM HasProducts Where HP_Dep_title='" + dep + "'")

myresult = mycursor.fetchall()
print("Users:")
for x in myresult:
  print(str(x[0])+"\t"+x[1])

mydb.close()

