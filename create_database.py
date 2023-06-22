import sqlite3

conn = sqlite3.connect('python_api.db')
cursor = conn.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
  id INTEGER PRIMARY KEY,
  title TEXT,
  author TEXT
);
""")

# Insert values into books table
cursor.execute("""
INSERT INTO books (id,title, author) VALUES
(1,'Book 1', 'Author 1'),
(2,'Book 2', 'Author 2'),
(3,'Book 3', 'Author 3'),
(4,'Book 4', 'Author 4'),
(5,'Book 5', 'Author 5');
""")

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  email TEXT,
  password TEXT
);
""")

# Insert values into users table
cursor.execute("""
INSERT INTO users (id, email, password) VALUES
(1,'user1@gmail.com', 'password1'),
(2,'user2@gmail.com', 'password2'),
(3,'user3@gmail.com', 'password3'),
(4,'user4@gmail.com', 'password4'),
(5,'user5@gmail.com', 'password5');
""")

# Commit changes and close the connection
conn.commit()
conn.close()
