import asyncio

from dotenv import load_dotenv

from agent.flow import ask_name


load_dotenv()

async def main():
    response = await ask_name()
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
