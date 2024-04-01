import asyncio

async def greet(name):
    print(f"Hello {name}!")

asyncio.run(greet("world"))
