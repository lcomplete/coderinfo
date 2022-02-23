#coding=utf-8

from capture.torndb import Connection

DB_CONFIG = {
    'db': 'cinfo',
    'host': 'localhost',
    'user': 'lcomplete',
    'pass': '123abc456'
}

def get_db():
    db = Connection(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['pass'],
        database=DB_CONFIG['db']

        # time_zone="+8:00"
    )
    return db
