from tinydb import TinyDB

db = TinyDB("test_db.json")
templates_table = db.table("templates")
