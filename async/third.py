# Creating tasks explicitly: Tasks start running immediately
# create_task = fire immediately
# gather = structured waiting
# time python3 third.py => Executed in  1.07 secs

import asyncio

async def task(name):
    await asyncio.sleep(1)
    print(f"{name} done")

async def main():
    t1 = asyncio.create_task(task("A"))
    t2 = asyncio.create_task(task("B"))

    print("Tasks created")
    await t1
    await t2

asyncio.run(main())
