def build_capacity(number, max_capacity, cabinet_count):
    percent = number / (max_capacity * cabinet_count)
    if percent == 0:
        return '[□□□□□] 无人'
    elif 0 < percent <= 0.2:
        return '[■□□□□] 舒适'
    elif 0.2 < percent <= 0.4:
        return '[■■□□□] 良好'
    elif 0.4 < percent <= 0.6:
        return '[■■■□□] 一般'
    elif 0.6 < percent <= 0.8:
        return '[■■■■□] 较拥挤'
    elif percent > 0.8:
        return '[■■■■■] 十分拥挤'

def build_msg(data: dict):
    item = f'''[{data['name']}]
地区：{data['region']}
别名：{data['command']}
机台数量：{data['cabinetCount']}
当前人数：{data['playerCount']}人
拥挤度：{build_capacity(data['playerCount'], data['maxCapacity'], data['cabinetCount'])}
更新时间：{data['updateTime']}

'''
    return {
        "type": "text",
        "data": {
            "text": f"{item}"
        }
    }