import pymysql
from db_config import host_name, username, password, database_name

db = pymysql.connect(
    host = host_name,
    port = 7887,
    user = username,
    passwd = password,
    db = database_name,
    charset = 'utf8'
)

# cursor = db.cursor()
# cursor.execute('set names utf8')
# db.commit()

