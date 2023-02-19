# command in terminal deadlines.db to create database 

# interact with database using sqlite3
import sqlite3

# connecting to the SQLite database by creating a Connection object
conn = sqlite3.connect('database.db')

# creating a Cursor object by calling the cursor() method on the Connection object
# Cursor object is used to execute SQL commands

cursor = conn.cursor()

# 1) Create Table
# create table in the database by executing an SQL command using the execute() method of the Cursor object
# create a table named tasks with (for example) three columns (user id, name of task, and deadline)
cursor.execute('''CREATE TABLE tasks
                  (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   task_name TEXT,
                   deadline DATE)''')

# 2) Add data
# Inserting data into table using SQL INSERT command
# Python variables to insert dynamic data into the table
# For example, to insert a new task with a name of 'Health Appointment' and a deadline of '2023-02-26'
cursor.execute("INSERT INTO tasks (task_name, deadline) VALUES (?, ?)", ('Health Appointment', '2023-02-26'))

# 3) Update data 
# write an SQL query to update a row in the table
query = "UPDATE tasks SET column_name = ? WHERE id = ?"
# column_name with the name of the column to be updated, id with the unique identifier of the row to be updated
params = ('new_value', 1) #Pass parameters to the query using a tuple
# replace 'new_value' with updated value for column, 1 with the ID of the row to be updated
cursor.execute(query, params) # execute query
conn.commit() # commit changes to db



# 4) Retrieve data 
# Retrieving data from the table using SQL SELECT command
# execute the command using the execute() method of the Cursor object,
# then fetch the results for example using the fetchall() method
# To retrieve one task from table:

# Step 1: Execute a SELECT query
query = "SELECT * FROM my_table WHERE id = ?"  # Define the SQL query string:
# sets the variable query to a string that contains an SQL query
# In this case all columns from the table my_table where id column equals a specific value
# ? is a placeholder for a value that will be passed in as a parameter later
params = (1,)  # Define the query parameters:
# sets the variable params to a tuple containing the value(s) to replace the ? placeholder(s) in query string
# In this case there is only one placeholder, so tuple contains one value: 1
cursor.execute(query, params)  # execute the query:
# uses cursor object created in Step 2 to execute the SQL query with the provided parameters
# result is stored in the cursor object for use in later steps

# Step 2: Retrieve the result
result = cursor.fetchone()

# Step 3: Print the result
print(result)



# After interaction with database: Close the cursor and connection
cursor.close()
conn.close()