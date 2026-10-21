import asyncio
import time

async def fetch_data(name: str, delay: int) -> str:
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)
    print(f"Done {name}")
    return f"Result from {name}"


async def main():
    print("=== Part 1: Sequential Execuation (Await one by one) ===")
    start_time = time.time()

    await fetch_data("Task A", 2)
    await fetch_data("Task B", 3)
    await fetch_data("Task C", 1)

    end_time = time.time()
    sequential_duration = end_time - start_time
    print(f"Sequential execution took: {sequential_duration:.2f} seconds\n")


    print("=== Part 2: Cocurrent Execuation (asyncio.gather) ===")
    start_time = time.time()


    results = await asyncio.gather(
        fetch_data("Task A", 2),
        fetch_data("Task B", 3),
        fetch_data("Task C", 1)
    )

    end_time = time.time()
    concurrent_duration = end_time - start_time
    print(f"Concurrent execution took: {concurrent_duration:.2f} seconds\n")


    print("=== Summary ===")
    print(f"Sequential time (Sum of delays): {sequential_duration:.2f} seconds")
    print(f"Concurrent time (Max delay): {concurrent_duration:.2f} seconds")
    print(f"Speedup Proof: Concurrency saved about {sequential_duration - concurrent_duration:.2f} seconds!")


if __name__ == "__main__":
    asyncio.run(main())