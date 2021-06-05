import pymysql
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "db": "test_YCC",
    "charset": "utf8"
}

# 建立Connection物件
db = pymysql.connect(**db_settings)
# 建立Cursor物件
cursor = db.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS log (id INT AUTO_INCREMENT, Date VARCHAR(255), Time VARCHAR(255), usec VARCHAR(255), SourceIP VARCHAR(255), SourcePort VARCHAR(255), DestinationIP VARCHAR(255), DestinationPort VARCHAR(255), DNS_A_record_query VARCHAR(255), PRIMARY KEY(id))')


