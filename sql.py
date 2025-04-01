import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Corrected SQL Query for Table Creation
table_info = """
CREATE TABLE student(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert Records
cursor.execute("INSERT INTO student VALUES ('SAI', 'CSE', 'A', 95)")
cursor.execute("INSERT INTO student VALUES ('LAXMI', 'ECE', 'B', 85)")
cursor.execute("INSERT INTO student VALUES ('TUMU', 'MECH', 'C', 76)")
cursor.execute("INSERT INTO student VALUES ('LATHA', 'DATASCIENCE', 'B', 87)")
cursor.execute("INSERT INTO student VALUES ('VASU', 'ML', 'A', 93)")
cursor.execute("INSERT INTO student VALUES ('VYSH', 'AI', 'C', 76)")
cursor.execute("INSERT INTO student VALUES ('RAO', 'ECE', 'B', 87)")

# Print Data
print("Selected records are:")

# Corrected SELECT statement (table name should be `student`)
data = cursor.execute("SELECT * FROM student")

for row in data:
    print(row)

# Commit & Close Connection
connection.commit()
connection.close()
