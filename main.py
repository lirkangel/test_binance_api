from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from decouple import config
import aiohttp
import asyncio
import time

print('for pair XRP/USDT')
async def main():
    n=0
    new_price = 0
    async with aiohttp.ClientSession() as session:
        while n > -1:
            binance_url = f"{config('API_BINANCE')}{config('PAIR')}"
            try:
                async with session.get(binance_url) as resp:
                    result = await resp.json()
                    current_price = result['price']
                    if new_price != current_price:
                        new_price = current_price
                        print(new_price)
                    time.sleep(1)
            except Exception as e:
                print(e)
                break
                        

asyncio.run(main())


# Чтобы доработать программу для многих пар думаю есть много способов, добавить api чтобы он добавил в программу также в env или же загрузить с Database
# смотря какая у вас инфраструктура 