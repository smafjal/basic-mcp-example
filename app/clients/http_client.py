import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/mcp/") as client:
        result = await client.call_tool("add", {"a": 10, "b": 5})
        print("Add Result:", result.structured_content['result'])

        result = await client.call_tool("subtract", {"a": 10, "b": 5})
        print("Subtract Result:", result.structured_content['result'])

        result = await client.call_tool("multiply", {"a": 10, "b": 5})
        print("Multiply Result:", result.structured_content['result'])

        result = await client.call_tool("divide", {"a": 10, "b": 5})
        print("Divide Result:", result.structured_content['result'])

        result = await client.call_tool("divide", {"a": 10, "b": 0})
        print("Divide Result:", result.structured_content['result'])

asyncio.run(main())
