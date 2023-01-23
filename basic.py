import asyncio

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print('finished')

async def main():
    print('mike')
    await foo('mike2')

# main()
# await main()

asyncio.run(main()) # event loop created





