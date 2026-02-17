import asyncio


async def hello():
    print("😴")
    await asyncio.sleep(1.0)
    print("Hello, World!")


main = hello

asyncio.run(main())