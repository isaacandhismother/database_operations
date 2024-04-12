import sqlite3
import random

books = {'Romeo and Juliett': 'tragedy',
         'Godfather': 'novel',
         'Data Tutashkhia': 'novel',
         'Neverhood': 'fairy tale',
         'History of World War 2': 'science fiction',
         'Bible': 'religion',
         'Introduction in Java': 'programming',
         'Me, myself and I': 'novel',
         'Red riding hood': 'fairy tale',
         'Chipollino': 'fairy tale'}

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute("""CREATE TABLE books(
            name TEXT,
            pages INT,
            cover TEXT,
            cetegory TEXT);
            """)

for book_name in books:
    pages = random.randint(50, 200)

    cover = random.choice(['A+', 'A', 'B', 'C', 'D'])

    category = books[book_name]

    cur.execute("INSERT INTO books VALUES('{}','{}','{}','{}')"
                .format(book_name, pages, cover, category))

cur.execute("SELECT * FROM books")

books = cur.fetchall()
print(books)

cur.execute("SELECT avg(pages) FROM books")
page = cur.fetchall()
print(f'Average page count: {page}')

cur.execute("SELECT name, pages FROM books WHERE pages = (SELECT max(pages) FROM books)")
max_page = cur.fetchall()
print(f'Book that has the most pages: {max_page}')

conn.commit()
