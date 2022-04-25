from mysql import create_db_connection
from nonebot.adapters import Event

def has_group(group_uim=None, module=None):
    if group_uim is None:
        return False
    dbc = create_db_connection()
    try:
        cursor = dbc.cursor()
        if module == 'maimaidx':
            query = "SELECT 1 FROM qun_maimaidx WHERE qun_uim = %s LIMIT 1"
        elif module == 'queue':
            query = "SELECT 1 FROM qun_queue WHERE qun_uim = %s LIMIT 1"
        else:
            return False
        cursor.execute(query, (group_uim))
        raw_data = cursor.fetchone()
        cursor.close()
        dbc.close()
        return False if raw_data is None else True
    except:
        dbc.close()
        return False

def get_group_uim(event: Event):
    session = str(event.get_session_id()).split('_')
    return session[1]
