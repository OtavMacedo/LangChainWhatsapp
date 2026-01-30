import asyncio

from dotenv import load_dotenv

from agent.flow import test_extractions



load_dotenv()

async def main():
    await test_extractions()


if __name__ == "__main__":
    asyncio.run(main())
