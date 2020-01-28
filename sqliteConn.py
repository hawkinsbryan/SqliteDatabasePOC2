import sqlite3
conn = sqlite3.connect('testingjson.db')

#load precompiled json1 extension
conn.enable_load_extension(True)
conn.load_extension("./json1")

# create a cursor
c = conn.cursor()

# make a table
# create table NAME_OF_TABLE (NAME_OF_FIELD TYPE_OF_FIELD);
c.execute('create table testtabledos (testfield JSON);')

# Insert a row of data into a table
c.execute("insert into testtabledos (testfield) values (json('{\"json1\": \"works\"}'));")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()