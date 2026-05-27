import asyncio
import time

#Coroutine
async def main():
    print("Hello")# print immediately
    # time.sleep(3) behave as synchronous
    await asyncio.sleep(3)#thread is idle 
    print("World")# This will be executed right after thread is idle 

asyncio.run(main())  