#!/usr/bin/env python3
""" The basics of async  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    Using the random module.  """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
