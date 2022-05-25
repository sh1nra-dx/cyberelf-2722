import aiohttp
import base64

async def cache40(payload):
    async with aiohttp.request("POST", "https://www.diving-fish.com/api/maimaidxprober/query/player", json=payload) as response:
        if response.status == 400:
            return 4001, "", ""
        elif response.status == 403:
            return 4031, "", ""
        body = base64.b64encode(bytes(str(await response.text()), 'utf-8'))
        obj = await response.json()
        data = {
            "type": "b40",
            "data": body.decode(),
        }
        async with aiohttp.request("POST", "https://api.rating.xbuster.moe/result/save.json", json=data) as response:
            if response.status != 200:
                return response.status, "", ""
            result = await response.json()
            id = result["resultId"]
            url = "https://rating.xbuster.moe/" + id
            return 200, obj["nickname"], url

async def cache50(payload):
    async with aiohttp.request("POST", "https://www.diving-fish.com/api/maimaidxprober/query/player", json=payload) as response:
        if response.status == 400:
            return 4001, "", ""
        elif response.status == 403:
            return 4031, "", ""
        body = base64.b64encode(bytes(str(await response.text()), 'utf-8'))
        obj = await response.json()
        data = {
            "type": "b50",
            "data": body.decode(),
        }
        async with aiohttp.request("POST", "https://api.rating.xbuster.moe/result/save.json", json=data) as response:
            if response.status != 200:
                return response.status, "", ""
            result = await response.json()
            id = result["resultId"]
            url = "https://rating.xbuster.moe/" + id
            return 200, obj["nickname"], url
