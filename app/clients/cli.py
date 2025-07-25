import argparse
import asyncio
from fastmcp import Client

async def call_tool(tool_name, a, b):
    async with Client("http://localhost:8000/mcp") as client:
        result = await client.call_tool(tool_name, {"a": a, "b": b})
    print(f"{tool_name.capitalize()} Result:", result.structured_content['result'])

def main():
    parser = argparse.ArgumentParser(description="MCP Calculator CLI")
    parser.add_argument("tool", choices=["add", "subtract", "multiply", "divide"], help="Tool name")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()
    asyncio.run(call_tool(args.tool, args.a, args.b))

if __name__ == "__main__":
    main()
