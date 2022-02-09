from mysql import create_db_connection

dbc = create_db_connection()
cursor = dbc.cursor()

try:
    query = "UPDATE shop SET player_count = 0, update_time = NOW()"
    cursor.execute(query)
    dbc.commit()
    print('清除队列缓存成功')
except:
    dbc.rollback()
    print('清除队列缓存失败')
