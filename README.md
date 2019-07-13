# joedb
# A simple database in python that is built on python dictionary and stored using json
 This is a simple Database implementation built on top of json
    The idea behind was found at https://medium.freecodecamp.org/how-to-write-a-simple-toy-database-in-python/
    by Palash Bauri

    The implementation is simple
    A database here is treated nothing more than a python dictionary.
    But after every change in the in memory dictionary database, the database is written to a file specified
    when creating an instance of the database object.
    This file can then be loaded back in memory when the database is called again after it has been deleted.

    Methods to be used are
    load(self, location)
            this loads the database file into a memory as dictionary

    get(self, key)
            this returns the value stored in memory with the key provided

    delete(self, key)
            This removes the key and related value from the database

    flush(self)
            This clears the entire database content

    dumpdb(self)
            This writes the dictionary in memory database to a file

    _load(self)
            An internal method that loads the database from file

    variables used are

    self.location
            This is the path and filename of the database file
            
# Example
-------------------------------
  mydb = joedb.JoeDb("mydb.db")
  mydb.set("Hello", "World")
  mydb.get("Hello")
   ##### outputs: "World"
