from mcp.server.fastmcp import FastMCP

# Create the MCP server and give it a name
mcp = FastMCP("Addition Server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


if __name__ == "__main__":
    mcp.run()   # runs over stdio by default