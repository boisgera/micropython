import asyncio
import inspect

async def _async_noop():
    pass

Generator = type(_async_noop)

def asyncify(async_function):
    if not inspect.iscoroutinefunction(async_function):
        function = async_function
        def async_function(*args, **kwargs):
            return function(*args, **kwargs)
    def _task(*args, **kwargs):
        coroutine = async_function(*args, **kwargs)
        if asyncio.get_event_loop().is_running():
            return asyncio.create_task(coroutine)
        else:
            asyncio.run(coroutine)
    return _task

@asyncify
async def greet(name):
    print(f"Hello {name}!")
    print(42)
    return 666

@asyncify
async def shuffle():
    print("*")
    await asyncio.sleep(0.0)

@asyncify
async def main():
    print("yup")
    await asyncio.sleep(3.0)
    p = greet("world")
    await shuffle()
    z = await p
    print(z)

main()
