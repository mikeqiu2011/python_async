import asyncio

async def main():
    print('main')
    task = asyncio.create_task(foo('foo'))
    # await task
    await asyncio.sleep(0.5) # will allow task to run first
    print('finished in main')

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print('finished in foo')


asyncio.run(main())  # event loop created
