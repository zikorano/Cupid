from config import ConfigManager
from datetime import *
from pony.orm import *

cm = ConfigManager()
db = Database()

dumyusers = {
    "A":{
        "first_name":"John",
        "last_name":"Doe",
        "bio":"Lorem ipsum",
        "dob":date(1990, 3, 17)
    },
    "B":{
        "first_name":"Jane",
        "last_name":"Doe",
        "bio":"Dolor et",
        "dob":date(1992, 6, 2)
    },
    "C":{
        "first_name":"Deez",
        "last_name":"Nutz",
        "bio":"Espeliamos",
        "dob":date(2002, 10, 22)
    }
}

class User(db.Entity):
    _table_    = "users"
    first_name = Required(str)
    last_name  = Required(str)
    bio        = Required(str)
    dob        = Required(date)

sql_debug(True)

db.bind(**cm.dbParams)
db.generate_mapping(create_tables=True)

@db_session
def create_dummy_users():
    for user in dumyusers.values():
        User(**user)
