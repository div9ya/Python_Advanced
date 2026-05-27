#Normal Synchronous
# import time


# def api_call():
#     time.sleep(3)
#     return "orders data"

# def execute():
#     print("Executing api call")
#     result=api_call()
#     print("Dta fetched: ",result)

# execute()    

#Asyncchronous
import asyncio
import time


async def api_call():
    await asyncio.sleep(3)
    return "orders data"

async def execute():
    print("Executing api call")
    result=await api_call()
    print("Data fetched: ",result)

asyncio.run(execute())    