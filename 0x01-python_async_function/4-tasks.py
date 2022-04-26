#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    """
    list_of_delays: List[float] = []
    delays_ascending: List[float] = []

    for i in range(n):
        list_of_delays.append(task_wait_random(max_delay))
    for item in asyncio.as_completed(list_of_delays):
        delays_ascending.append(await item)

    return delays_ascending
