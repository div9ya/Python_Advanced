import asyncio
import time


async def api_call(url:str,delay:int):
    print("Fetching data from ",url)
    await asyncio.sleep(delay)
    print("Data fetched from ",url)
    return f"{url} data"

async def main():
    #Creating tasks with gather
    tasks=await asyncio.gather(
        api_call("https://api.example.com/data1",5),
        api_call("https://api.example.com/data2",2),
        api_call("https://api.example.com/data3",4)
    )

    # tasks=[api_call(url) for url in ["https://api.example.com/data1",
    #                                  "https://api.example.com/data2",
    #                                  "https://api.example.com/data3"]]
    # result=await asyncio.gather(*tasks)
    print("All API calls completed. ")

asyncio.run(main())    