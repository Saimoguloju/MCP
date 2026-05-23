import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Resolve server path relative to this file — works from any working directory
SERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calculator_server.py")

OPERATIONS = {
    "1": ("add",      "+"),
    "2": ("subtract", "-"),
    "3": ("multiply", "*"),
    "4": ("divide",   "/"),
}

async def run_calculator():
    server_params = StdioServerParameters(
        command="python",
        args=[SERVER_PATH]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\n=============================")
            print("   MCP Calculator")
            print("=============================")

            while True:
                print("\nSelect operation:")
                for key, (name, symbol) in OPERATIONS.items():
                    print(f"  {key}. {name.capitalize()} ({symbol})")
                print("  5. Exit")

                choice = input("\nEnter choice (1-5): ").strip()

                if choice == "5":
                    print("Goodbye!")
                    break

                if choice not in OPERATIONS:
                    print("Invalid choice. Try again.")
                    continue

                try:
                    a = float(input("Enter first number : "))
                    b = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid number. Please enter digits only.")
                    continue

                tool_name, symbol = OPERATIONS[choice]

                try:
                    result = await session.call_tool(tool_name, {"a": a, "b": b})
                    answer = result.content[0].text
                    print(f"\nResult: {a} {symbol} {b} = {answer}")
                except Exception as e:
                    print(f"Error: {e}")

asyncio.run(run_calculator())