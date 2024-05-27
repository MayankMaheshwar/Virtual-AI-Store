import mysql.connector

# Connect to the database
conn = mysql.connector.connect(user='username', password='password', host='localhost', database='dbname')
cursor = conn.cursor()

# Sample data (replace with your actual data)
data = [(1, 'row1_data'), (2, 'row2_data'), ...]  # List of tuples containing data for each row

# Insert data in batches
batch_size = 1000
for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]
    cursor.executemany("INSERT INTO tablename (column1, column2) VALUES (%s, %s)", batch)
    conn.commit()

# Close cursor and connection
cursor.close()
conn.close()
