import asyncio
import time

# First task
async def api_call(url:str,delay:int=3):
    print("Fetching data from ",url)
    await asyncio.sleep(delay)
    print("Data fetched from ",url)

# Second task
async def execute():
    time.sleep(5)
    print("Execution completed")

# Third Task
async def transformation():
    asyncio.sleep(4)
    print("Data transformation completed")


async def main():
    #Creating tasks with gather
    await asyncio.gather(
        api_call("https://api.example.com/data1"),
        execute(),
        transformation(),
    )
    print("All API calls completed. ")

asyncio.run(main())