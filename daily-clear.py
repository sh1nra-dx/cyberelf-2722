from mysql import create_db_connection

dbc = create_db_connection()
try:
    cursor = dbc.cursor()
    select_query = "SELECT id FROM shop"
    update_query = "UPDATE shop SET player_count = 0, update_time = NOW() WHERE id = %s LIMIT 1"
    cursor.execute(select_query)
    ids = cursor.fetchall()
    for i in ids:
        cursor.execute(update_query, (ids[0]))
    dbc.commit()
    cursor.close()
    dbc.close()
    print('清除队列缓存成功')
except:
    dbc.rollback()
    dbc.close()
    print('清除队列缓存失败')
