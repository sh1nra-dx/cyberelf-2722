import aiohttp
import base64
import json
from src.libraries.maimaidx.maimai_best_50 import computeRa

async def cache40(payload):
    async with aiohttp.request("POST", "https://www.diving-fish.com/api/maimaidxprober/query/player", json=payload) as response:
        if response.status == 400:
            return 4001, "", ""
        elif response.status == 403:
            return 4031, "", ""
        r = await response.json()
        data = {
            "type": "b40",
            "data": base64.b64encode(bytes(str(json.dumps(r)), 'utf-8')).decode(),
        }
        async with aiohttp.request("POST", "https://api.rating.xbuster.moe/result/save.json", json=data) as response:
            if response.status != 200:
                return response.status, "", ""
            result = await response.json()
            id = result["resultId"]
            url = "https://rating.xbuster.moe/" + id
            return 200, r["nickname"], url

async def cache50(payload):
    async with aiohttp.request("POST", "https://www.diving-fish.com/api/maimaidxprober/query/player", json=payload) as response:
        if response.status == 400:
            return 4001, "", ""
        elif response.status == 403:
            return 4031, "", ""
        r = await response.json()
        b35 = []
        b15 = []
        for chart in r["charts"]["sd"]:
            ra = computeRa(chart["ds"], chart["achievements"])
            chart["ra"] = ra
            b35.append(chart)
        for chart in r["charts"]["dx"]:
            ra = computeRa(chart["ds"], chart["achievements"])
            chart["ra"] = ra
            b15.append(chart)
        r["charts"]["sd"] = b35
        r["charts"]["dx"] = b15
        data = {
            "type": "b50",
            "data": base64.b64encode(bytes(str(json.dumps(r)), 'utf-8')).decode(),
        }
        async with aiohttp.request("POST", "https://api.rating.xbuster.moe/result/save.json", json=data) as response:
            if response.status != 200:
                return response.status, "", ""
            result = await response.json()
            id = result["resultId"]
            url = "https://rating.xbuster.moe/" + id
            return 200, r["nickname"], url

