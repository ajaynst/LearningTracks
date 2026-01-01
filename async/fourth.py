import asyncio

async def slow():
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("Cancelled!")
        raise

async def main():
    task = asyncio.create_task(slow())

    await asyncio.sleep(1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Handled cancellation")

asyncio.run(main())
