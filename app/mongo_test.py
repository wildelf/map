#_author:sanny
#date:2018-05-08

import pymongo
import time

def insert_data():
    data = {'name':'wilde'}
    collection = connect_mongo('t1')
    data['timestamp'] = int(time.time())
    collection.insert_one(data)

# 连接mongo
def connect_mongo(db_name):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['test']
    collection = db[db_name]
    return collection

# 获取检测时间内的数据
def get_check_data():
    collection = connect_mongo('t1')
    now_time = int(time.time())
    find_time = now_time - 10
    cursor = collection.find({'timestamp': {'$gt': find_time}}, {"timestamp": 1}).limit(0)
    return cursor

# 获取上一个检测时间内的数据
def get_pre_check_data():
    collection = connect_mongo('t1')
    now_time = int(time.time())
    start_find_time = now_time - 20
    end_find_time = now_time - 10
    cursor = collection.find({'timestamp': {'$gt': start_find_time,'$lte':end_find_time}}, {"timestamp": 1}).limit(0)
    return cursor

for i in range(2):
    time.sleep(10)
    insert_data()


cursor = get_check_data()
if cursor.count():

    print('存在数据')
    if get_pre_check_data().count():
        print('该机器正常')
    else:
        print('该机器重连或是新机器')
else:
    print('该机器故障')


