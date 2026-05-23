import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movie_server.py")

MENU = """
╔══════════════════════════════════════╗
║     IMDB Top 100 Movie Recommender   ║
╠══════════════════════════════════════╣
║  1. Show Top N Movies                ║
║  2. Search by Genre                  ║
║  3. Search by Director               ║
║  4. Get Movie Details                ║
║  5. Get Recommendations              ║
║  6. Exit                             ║
╚══════════════════════════════════════╝
"""

async def run():
    server_params = StdioServerParameters(command="python", args=[SERVER_PATH])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print(MENU)

            while True:
                choice = input("Enter choice (1-6): ").strip()

                if choice == "1":
                    n = input("How many top movies to show? (1-100): ").strip()
                    try:
                        n = int(n)
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                    result = await session.call_tool("get_top_movies", {"limit": n})
                    print("\n" + result.content[0].text)

                elif choice == "2":
                    genre = input("Enter genre (e.g. Drama, Action, Sci-Fi, Horror, Western): ").strip()
                    result = await session.call_tool("search_by_genre", {"genre": genre})
                    print("\n" + result.content[0].text)

                elif choice == "3":
                    director = input("Enter director name: ").strip()
                    result = await session.call_tool("search_by_director", {"director": director})
                    print("\n" + result.content[0].text)

                elif choice == "4":
                    title = input("Enter movie title (partial match works): ").strip()
                    result = await session.call_tool("get_movie_details", {"title": title})
                    print("\n" + result.content[0].text)

                elif choice == "5":
                    genre = input("Enter genre to filter (leave blank for all): ").strip()
                    min_rating_str = input("Minimum IMDB rating (e.g. 8.5): ").strip()
                    limit_str = input("How many recommendations? (e.g. 5): ").strip()
                    try:
                        min_rating = float(min_rating_str) if min_rating_str else 8.0
                        limit = int(limit_str) if limit_str else 5
                    except ValueError:
                        print("Invalid input for rating or limit.")
                        continue
                    result = await session.call_tool(
                        "recommend_movies",
                        {"genre": genre, "min_rating": min_rating, "limit": limit}
                    )
                    print("\n" + result.content[0].text)

                elif choice == "6":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Enter a number between 1 and 6.")

                print()

asyncio.run(run())
