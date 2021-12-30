import mysql.connector
from sql_operations import *

tracker = mysql.connector.connect(
  host="localhost",
  user="tracker_user",
  password="TrackerUser49",
  database="tracker"
)
while(True):
  cursor = tracker.cursor()
  op = input("What would you like to do? (insert, delete, display, edit, resolve, exit): ")
  if(op.lower() == "insert"):
    insert(tracker, cursor)
  elif(op.lower() == "delete"):
    delete(tracker, cursor)
  elif(op.lower() == "display"):  
    select(cursor)
  elif(op.lower() == "edit"):  
    edit(tracker, cursor)
  elif(op.lower() == "resolve"):  
    resolve(tracker, cursor)  
  elif(op.lower() == "exit"):  
    break
  else:
    print("That is not a valid option! Please try again.")
print("Goodbye.")
