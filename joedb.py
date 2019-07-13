import os
import json



"""
**********************************************************************************
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
**********************************************************************************
"""
class JoeDb(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)    # This is the path and filename of the database file
        self.load(self.location) 

    def __repr__(self):
        return "JoeDb database at {}".format(str(self.location))
    
    def load(self, location):
        """  Loads the database from file into memory if file exists  by calling _load(self) else, ccreates a new one"""
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        """ Loads the database file into memory using json"""
        self.db = json.load(open(self.location, 'r'))

    def dumpdb(self):
        """ Writes the memory database content into a file """
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False

    def set(self, key, value):
        """ Adds the key value pair to database """
        try:
            self.db[str(key).encode()] = value.encode()
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : "+str(e))
            return False

    def get(self, key):
        """ Gets the value corresponding to the key """
        try:
            return self.db[key.encode()].decode()
        except KeyError:
            print("No Value Can Be Found for "+ str(key))
            return False

    def get_all(self):
        """ Returns all key value pairs in database """
        return self.db
    
    def delete(self, key):
        """ removes the key and related value pair from database"""
        if not key.encode() in self.db:
            return False
        else:
            del self.db[key.encode()]
            self.dumpdb()
            return True

    def flush(self):
        """ Clears entire database """
        a = input("Do you really want to do that? \n"
                  "Enter Y for yes or any other input for No")
        if not a=="Y" or a == "y":
            self.db = {}
            self.dumpdb()
            return True
        return "Flush Aborted"
