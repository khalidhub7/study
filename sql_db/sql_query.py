import MySQLdb

# Establish a connection to the MySQL database
db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database_name")

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Define the SQL query (corrected syntax and table name)
sql_query = "SELECT * FROM cars WHERE fuel = 'on'"

# Execute the SQL query
cursor.execute(sql_query)

# Fetch all the rows from the result set
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
