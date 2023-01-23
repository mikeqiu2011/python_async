import asyncio


async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('finished fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    result = await task1  # return value from a future
    print(result)
    await task2


asyncio.run(main())
