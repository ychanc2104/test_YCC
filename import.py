import pymysql
import numpy as np
import pandas as pd
import datetime

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "chang951",
    "db": "test_YCC",
    "charset": "utf8"
}

path = r'dns_sample.csv'
df = pd.read_csv(path, error_bad_lines=False)
n = df.shape[0]
timestamp = np.array(df['frame.time_epoch'])
IP = np.array(df['ip.src'])
Port = np.array(df['udp.srcport'])
DesIP = np.array(df['ip.dst'])
DesPort = np.array(df['udp.dstport'])
DNS = np.array(df['dns.qry.name'])

db = pymysql.connect(**db_settings)

cursor = db.cursor()

for i in range(n):
    
    date_full = datetime.datetime.fromtimestamp(timestamp[i])
    Date = date_full.strftime('%Y-%m-%d')
    Time = date_full.strftime('%H:%M')
    usec = date_full.strftime('%S')
    SourceIP = IP[i]
    SourcePort = str(Port[i])
    DestinationIP = DesIP[i]
    DestinationPort = str(DesPort[i])
    FQDN = DNS[i]
    sql = "INSERT INTO log_ori (Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, DNS_A_record_query) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    
    cursor.execute(sql, (Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN))
    #cursor.execute('SELECT LAST_INSERT_ID() AS "log_id"')    
    # 提交修改
    db.commit()
    print(f'success {i}')
    
        # 發生錯誤時停止執行SQL
    #db.rollback()
    #    print(SourceIP)

db.close()


#資料表相關操作

