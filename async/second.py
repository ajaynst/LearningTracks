# True concurrency with asyncio.gather() - Schedule coroutines together
# time python3 second.py => Executed in  2.06 secs

import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 2),
    )

asyncio.run(main())
