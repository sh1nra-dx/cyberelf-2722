from mysql import create_db_connection

def get_all(group_uim=None):
    dbc = create_db_connection()
    try:
        cursor = dbc.cursor()
        query = "SELECT shop.*, region.region_name FROM qun_queue LEFT JOIN queue_region USING (region_id) LEFT JOIN queue_shop USING (region_id) WHERE qun_queue.qun_uim = %s ORDER BY shop_id ASC"
        cursor.execute(query, (group_uim))
        raw_data = cursor.fetchall()
        queue_list = []
        for d in raw_data:
            queue_list.append({
                'name': d[2],
                'command': d[3],
                'cabinetCount': d[4],
                'maxCapacity': d[5],
                'playerCount': d[6],
                'updateTime': d[7].strftime('%Y-%m-%d %H:%M:%S'),
                'region': d[8],
            })
        cursor.close()
        dbc.close()
        return {
            'error': False,
            'list': queue_list,
        }
    except:
        dbc.close()
        return {
            'error': True,
            'msg': '数据查询失败，请稍后再试',
        }

def get_one(command, group_uim=None):
    dbc = create_db_connection()
    try:
        cursor = dbc.cursor()
        query = "SELECT shop.*, region.region_name FROM qun_queue LEFT JOIN queue_region USING (region_id) LEFT JOIN queue_shop USING (region_id) WHERE qun_queue.qun_uim = %s AND queue_shop.command = %s LIMIT 1"
        cursor.execute(query, (group_uim, command))
        raw_data = cursor.fetchone()
        queue_info = {
            'name': raw_data[2],
            'command': raw_data[3],
            'cabinetCount': raw_data[4],
            'maxCapacity': raw_data[5],
            'playerCount': raw_data[6],
            'updateTime': raw_data[7].strftime('%Y-%m-%d %H:%M:%S'),
            'region': raw_data[8],
        }
        cursor.close()
        dbc.close()
        return {
            'error': False,
            'info': queue_info,
        }
    except:
        dbc.close()
        return {
            'error': True,
            'msg': '数据更新失败，请稍后再试',
        }

def set_player(command, number, group_uim=None):
    dbc = create_db_connection()
    try:
        cursor = dbc.cursor()
        select_query = "SELECT queue_shop.* FROM qun_queue LEFT JOIN queue_region USING (region_id) LEFT JOIN queue_shop USING (region_id) WHERE qun_queue.qun_uim = %s AND queue_shop.command = %s LIMIT 1"
        cursor.execute(select_query, (group_uim, command))
        raw_data = cursor.fetchone()
        shop_id = raw_data[0]
        number = int(number)
        player_count = 0 if number <= 0 else number
        update_query = "UPDATE queue_shop SET player_count = %s, update_time = NOW() WHERE shop_id = %s LIMIT 1"
        cursor.execute(update_query, (player_count, shop_id))
        dbc.commit()
        select_query = "SELECT queue_shop.*, queue_region.region_name FROM queue_shop LEFT JOIN queue_region USING (region_id) WHERE queue_shop.shop_id = %s LIMIT 1"
        cursor.execute(select_query, (shop_id))
        raw_data = cursor.fetchone()
        queue_info = {
            'name': raw_data[2],
            'command': raw_data[3],
            'cabinetCount': raw_data[4],
            'maxCapacity': raw_data[5],
            'playerCount': raw_data[6],
            'updateTime': raw_data[7].strftime('%Y-%m-%d %H:%M:%S'),
            'region': raw_data[8],
        }
        cursor.close()
        dbc.close()
        return {
            'error': False,
            'info': queue_info,
        }
    except:
        dbc.rollback()
        dbc.close()
        return {
            'error': True,
            'msg': dbc.er,
        }
