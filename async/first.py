# this will take 4 sec for exec, not async even though async is given
# time python3 first.py => Executed in  4.07 secs

import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")

async def main():
    await task("A", 2)
    await task("B", 2)

asyncio.run(main())