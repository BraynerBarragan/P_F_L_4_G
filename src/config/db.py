import mariadb

config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'parcial2_l4g'
}
DB = mariadb.connect(**config)
DB.autocommit = True
