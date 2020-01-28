import sqlite3
print(sqlite3.sqlite_version)

# CRUD Operations
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dummy")
    for row in cursor:
        print({row})
    print()


def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO dummy(A,B) VALUES(?,?)',
        (3232, 'catzzz')
    )
    conn.commit()
    read(conn)


def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE dummy SET B = ? WHERE A = ?',
        ('dogzzz', 3232)
    )
    conn.commit()
    read(conn)


def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM dummy WHERE A > 5'
    )
    conn.commit()
    read(conn)


# Create table
def create_table(conn):
    # Create table
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS dummy(
            A INTEGER PRIMARY KEY,
            B TEXT
        )
        """
    )

    # Table is empty? Insert dummy data
    res = conn.execute('SELECT * FROM dummy')
    if res.fetchone() is None:
        ins_str = """
            INSERT INTO Dummy(A,B) VALUES(?,?)
        """
        conn.execute(ins_str, (1, 'Ball'))
        conn.execute(ins_str, (2, 'Pen'))
        conn.execute(ins_str, (3, 'Computer'))
        conn.execute(ins_str, (4, 'Orange'))
        conn.execute(ins_str, (5, 'Dog'))

    conn.commit()


# -----------------------------------------

# Create and connect to a SQLite DataBase
conn = sqlite3.connect('myDB.db')

# Create table
create_table(conn)

# CRUD Operations
read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()