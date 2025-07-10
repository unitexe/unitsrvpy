import asyncio

from unitsrvpy.server import Server


async def main_async():
    print("Application started")
    server = Server()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(server.run_async())


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
