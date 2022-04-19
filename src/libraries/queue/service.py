from mysql import create_db_connection

def has_group(group_uim=None):
    if group_uim is None:
        return False
    else:
        dbc = create_db_connection()
        try:
            cursor = dbc.cursor()
            query = "SELECT 1 FROM qun WHERE qun_uim = %s LIMIT 1"
            cursor.execute(query, (group_uim))
            raw_data = cursor.fetchone()
            cursor.close()
            dbc.close()
            return False if raw_data is None else True
        except:
            dbc.close()
            return False

def get_all(group_uim=None):
    if not has_group(group_uim):
        return {
            'error': True,
            'msg': '当前群组未开通此功能，请联系管理员绑定',
        }
    else:
        dbc = create_db_connection()
        try:
            cursor = dbc.cursor()
            query = "SELECT shop.*, region.region_name FROM qun LEFT JOIN region USING (region_id) LEFT JOIN shop USING (region_id) WHERE qun.qun_uim = %s ORDER BY shop_id ASC"
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
    if not has_group(group_uim):
        return {
            'error': True,
            'msg': '当前群组未开通此功能，请联系管理员绑定',
        }
    else:
        dbc = create_db_connection()
        try:
            cursor = dbc.cursor()
            query = "SELECT shop.*, region.region_name FROM qun LEFT JOIN region USING (region_id) LEFT JOIN shop USING (region_id) WHERE qun.qun_uim = %s AND shop.command = %s LIMIT 1"
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

def add_player(command, number, group_uim=None):
    if not has_group(group_uim):
        return {
            'error': True,
            'msg': '当前群组未开通此功能，请联系管理员绑定',
        }
    else:
        dbc = create_db_connection()
        try:
            cursor = dbc.cursor()
            select_query = "SELECT shop.* FROM qun LEFT JOIN region USING (region_id) LEFT JOIN shop USING (region_id) WHERE qun.qun_uim = %s AND shop.command = %s LIMIT 1"
            cursor.execute(select_query, (group_uim, command))
            raw_data = cursor.fetchone()
            shop_id = raw_data[0]
            player_count = raw_data[6]
            player_count += int(number)
            update_query = "UPDATE shop SET player_count = %s, update_time = NOW() WHERE shop_id = %s LIMIT 1"
            cursor.execute(update_query, (player_count, shop_id))
            dbc.commit()
            select_query = "SELECT shop.*, region.region_name FROM shop LEFT JOIN region USING (region_id) WHERE shop.shop_id = %s LIMIT 1"
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

def del_player(command, number, group_uim=None):
    if not has_group(group_uim):
        return {
            'error': True,
            'msg': '当前群组未开通此功能，请联系管理员绑定',
        }
    else:
        dbc = create_db_connection()
        try:
            cursor = dbc.cursor()
            select_query = "SELECT shop.*, region.region_name FROM qun LEFT JOIN region USING (region_id) LEFT JOIN shop USING (region_id) WHERE qun.qun_uim = %s AND shop.command = %s LIMIT 1"
            cursor.execute(select_query, (group_uim, command))
            raw_data = cursor.fetchone()
            shop_id = raw_data[0]
            player_count = raw_data[6]
            if (player_count - int(number)) <= 0:
                player_count = 0
            else:
                player_count -= int(number)
            update_query = "UPDATE shop SET player_count = %s, update_time = NOW() WHERE shop_id = %s LIMIT 1"
            cursor.execute(update_query, (player_count, shop_id))
            dbc.commit()
            select_query = "SELECT shop.*, region.region_name FROM shop LEFT JOIN region USING (region_id) WHERE shop.shop_id = %s LIMIT 1"
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
                'msg': '数据更新失败，请稍后再试',
            }
