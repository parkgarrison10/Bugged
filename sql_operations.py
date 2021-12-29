from datetime import datetime

def insert(database, cursor): #used to insert a bug into the sql database
    insert_bug = ("INSERT INTO bugs"
             "(description, project, priority, entry_date, resolved)" 
             "VALUES (%s, %s, %s, %s, %s)")

    description = input("Enter the bug description: ")

    project = input("Enter the project that the bug is present in: ")

    priority = input("Enter the priority of the bug (high, medium, low): ")
    
    now = datetime.now()

    data_bug = (description, project, priority, now.strftime("%m/%d/%Y, %H:%M:%S"), 0)

    cursor.execute(insert_bug, data_bug)
    database.commit()

def delete(database, cursor): #deletes an entry from the database
    select(cursor)
    id = (input("Enter the id you'd like to delete: "), )

    delete_bug = "DELETE FROM bugs WHERE id = %s"

    cursor.execute(delete_bug, id)

    database.commit()

def edit(database, cursor):
    print("not yet implemented")

def resolve(database, cursor):
    select(cursor)
    id = (input("Enter the id you'd like to resolve: "), )

    resolve_bug = "UPDATE bugs SET resolved = '1' WHERE id = %s"

    cursor.execute(resolve_bug, id)

    database.commit()

    
def select(cursor): #used to print all bugs in the database
    cursor.execute("SELECT * FROM bugs")

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
