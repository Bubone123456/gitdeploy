from mcp.server.fastmcp import FastMCP

mcp = FastMCP("deploy")

@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two integers."""
    return x + y