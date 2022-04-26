<p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/holberton-logo.png" alt="holberton" /></a></p>
  
  <p align="center">
    <a href="https://twitter.com/juanoso07555284" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juanoso07555284" height="30" width="40" /></a>
  <a href="https://linkedin.com/in/juan-camilo-bocanegra-osorio-18b1821a6" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="juan-camilo-bocanegra-osorio-18b1821a6" height="30" width="40" /></a>
  </p>

0x02. Python - Async Comprehension
==================================

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220426%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220426T173249Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=879888aca7b520c4cf8cae2dd5b53045e4e285c52598f955e7db508d7b14a9f5)

Resources
---------

**Read or watch**:

*   [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
*   [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
*   [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

*   How to write an asynchronous generator
*   How to use async comprehensions
*   How to type-annotate generators

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5.x)
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions and coroutines must be type-annotated.

Tasks
-----

### 0\. Async Generator

Mandatory

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

``` bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

**Repo:**

*   GitHub repository: [`holbertonschool-backend-python`](https://github.com/jbocane6/holbertonschool-backend-python)
*   Directory: [`0x02-python_async_comprehension`](/0x02-python_async_comprehension)
*   File: [`0-async_generator.py`](0-async_generator.py)

-----
### 1\. Async Comprehensions

Mandatory

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

``` bash
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

**Repo:**

*   GitHub repository: [`holbertonschool-backend-python`](https://github.com/jbocane6/holbertonschool-backend-python)
*   Directory: [`0x02-python_async_comprehension`](/0x02-python_async_comprehension)
*   File: [`1-async_comprehension.py`](1-async_comprehension.py)

-----
### 2\. Run time for four parallel comprehensions

Mandatory

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

``` bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135
```    

**Repo:**

*   GitHub repository: [`holbertonschool-backend-python`](https://github.com/jbocane6/holbertonschool-backend-python)
*   Directory: [`0x02-python_async_comprehension`](/0x02-python_async_comprehension)
*   File: [`2-measure_runtime.py`](2-measure_runtime.py)

-----
Copyright © 2022 Holberton Inc, All rights reserved.