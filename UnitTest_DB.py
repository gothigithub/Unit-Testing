import mysql.connector
from mysql.connector import errorcode
import utils
from mock_db import MockDB
from mock import patch
from typing import List, Dict


config = {
    'host': MYSQL_HOST,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': MYSQL_DB
}


class ConnectionDatabase(Exception):
    """Raised when the database connection fails."""
    connected = False
    def connect_to_db(self): # (connection_string: str):
    with patch('connect_to_db') as mocked_get:
        mocked_get.return_value.ok = True
   
    print("connection string: ", connection_string)
    if connection_string == "test":
        raise TestDbError("ERROR: YOU FORGOT TO MOCK connect_to_db")
    else:
        raise ConnectionDatabaseError("Can't connect to the database!")
try:
    connection_string = MySQLdb.connect(host="MYSQL_HOST", user="MYSQL_USER", password="MYSQL_PASSWORD", db="MYSQL_DB")
        connected  = True
except MySQLError as ex:
    print("'not connected'pass")
if connected:
    print("'connected' pass")

    
  

class Database:
    def __init__(self,username,birthday,role):
        self.username = username
        self.birthday = birthday
        self.role     = role
        self.connect  = connection_string
    
    @property
    def connect(self):
        return 'f{}(self.username)




def get_users_list_from_db(connection_string: str) -> List[Dict[str, str]]:

    db = connect_to_db(connection_string)
    users = db.get_user()
    return users.database ('{} {} {}'.format)
    self.assertEqual
    self.assertEqual
