import asyncio

async def main():
    print('mike')
    task = asyncio.create_task(foo('mike2')) # only do this after all
    # sequential code is done
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(main())  # event loop created
