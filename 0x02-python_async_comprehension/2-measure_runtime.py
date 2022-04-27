#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
Measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Will execute async_comprehension 4 times in parallel using asyncio.gather.
    """
    start_time = perf_counter()
    comprehensions = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*comprehensions)
    final_time = perf_counter()
    return final_time - start_time
