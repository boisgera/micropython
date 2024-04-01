# MicroPython Async

**⚠️ Warning.** Conda-forge and snap install of micropython couldn't import the
`asyncio` module, maybe because they refer to old version of micropython (?). 
So, I tried to build micropython from the source
available on the [Download] page (version 1.22.2 ATM),
using the instructions from the [Getting Started] document.
However, that failed with the following error:

```console
boisgera@wreck:~/Downloads/micropython-1.22.2/ports/unix$ make submodules
Use make V=1 or set BUILD_VERBOSE in your environment to increase build verbosity.
Updating submodules: lib/mbedtls lib/berkeley-db-1.xx lib/micropython-lib
fatal: not a git repository (or any of the parent directories): .git
make: *** [../../py/mkrules.mk:253: submodules] Error 128
```

So, let's build from the git repo. OK, no issue there, after the build and
the copy of the whole build-standard repo where I want it and the `PATH`
variable update, I can work with the `asyncio` module.

```console
$ micropython
MicroPython v1.23.0-preview.322.g5114f2c1e on 2024-04-01; linux [GCC 9.4.0] version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> import asyncio
>>>
```






[Download]: https://micropython.org/download/
[Getting Started]: https://docs.micropython.org/en/latest/develop/gettingstarted.html

--------------------------------------------------------------------------------

```python
# file: main.py
async def greet(name):
    print(f"Hello {name}!")

greet("world")
```

```console
$ micropython main.py
"Hello world!"
```


```python
# file: main.py
async def greet(name):
    print(f"Hello {name}!")

greet("world")
```

```console
$ micropython main.py
```

Whoot?

```python
# file: main.py
async def greet(name):
    print(f"Hello {name}!")

print(greet("world"))
```

```console
$ micropython main.py
<generator object 'greet' at 7f023b50c3a0>
```

