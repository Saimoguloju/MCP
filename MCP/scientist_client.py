import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scientist_server.py")

MENU = """
╔══════════════════════════════════════════════╗
║      World Top 500 Scientists Explorer       ║
╠══════════════════════════════════════════════╣
║  1. Get Scientist Details (by name)          ║
║  2. Search by Country                        ║
║  3. Search by Field                          ║
║  4. Search by Invention / Discovery          ║
║  5. Nobel Prize Winners                      ║
║  6. Show Top N Scientists                    ║
║  7. Database Statistics                      ║
║  8. Exit                                     ║
╚══════════════════════════════════════════════╝
"""

async def run():
    server_params = StdioServerParameters(command="python", args=[SERVER_PATH])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print(MENU)

            while True:
                choice = input("Enter choice (1-8): ").strip()

                if choice == "1":
                    name = input("Enter scientist name (or partial): ").strip()
                    result = await session.call_tool("get_scientist_details", {"name": name})
                    print("\n" + result.content[0].text)

                elif choice == "2":
                    country = input("Enter country (e.g. Germany, India, USA, Japan): ").strip()
                    result = await session.call_tool("search_by_country", {"country": country})
                    print("\n" + result.content[0].text)

                elif choice == "3":
                    print("Fields: Physics, Chemistry, Biology, Medicine, Mathematics,")
                    print("        Computing, AI, Astronomy, Engineering, Earth Sciences,")
                    print("        Economics, Psychology, Genetics, Neuroscience")
                    field = input("Enter field: ").strip()
                    result = await session.call_tool("search_by_field", {"field": field})
                    print("\n" + result.content[0].text)

                elif choice == "4":
                    kw = input("Enter keyword (e.g. quantum, vaccine, DNA, electricity, laser): ").strip()
                    result = await session.call_tool("search_by_invention", {"keyword": kw})
                    print("\n" + result.content[0].text)

                elif choice == "5":
                    print("Filter by field (leave blank for all Nobel winners):")
                    print("Options: Physics, Chemistry, Medicine, Economics, Peace")
                    field = input("Field (or press Enter for all): ").strip()
                    result = await session.call_tool("get_nobel_prize_winners", {"field": field})
                    print("\n" + result.content[0].text)

                elif choice == "6":
                    n = input("How many scientists to show? (1-500): ").strip()
                    try:
                        n = int(n)
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                    result = await session.call_tool("get_top_scientists", {"limit": n})
                    print("\n" + result.content[0].text)

                elif choice == "7":
                    result = await session.call_tool("get_statistics", {})
                    print("\n" + result.content[0].text)

                elif choice == "8":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Enter a number between 1 and 8.")

                print()

asyncio.run(run())
