from fastmcp import FastMCP

mcp = FastMCP("CalculatorMCP", instructions="A simple calculator MCP with basic arithmetic operations.")


@mcp.tool
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first."""
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divides the first number by the second."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


if __name__ == "__main__":
    """When using Stdio transport, you will typically not run the server yourself as a separate process. 
    Rather, your clients will spin up a new server process for each session. 
    As such, no additional configuration is required."""
    # mcp.run(transport="stdio") 

    mcp.run(transport="http", host="localhost", port=8000)

