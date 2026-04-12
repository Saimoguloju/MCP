import os
import sys
import json
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not TAVILY_API_KEY:
    print("ERROR: TAVILY_API_KEY not found in .env", file=sys.stderr)
    sys.exit(1)
if not GROQ_API_KEY:
    print("ERROR: GROQ_API_KEY not found in .env", file=sys.stderr)
    sys.exit(1)

mcp = FastMCP("Tavily Search Server")


@mcp.tool()
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web using Tavily API and return results."""
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": max_results,
        "search_depth": "basic",
        "include_answer": True,
    }
    response = httpx.post(url, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    results = []
    if data.get("answer"):
        results.append(f"Quick Answer: {data['answer']}\n")

    for i, result in enumerate(data.get("results", []), 1):
        results.append(
            f"{i}. {result.get('title', 'No title')}\n"
            f"   URL: {result.get('url', '')}\n"
            f"   {result.get('content', '')[:300]}...\n"
        )

    return "\n".join(results) if results else "No results found."


@mcp.tool()
def search_and_answer(question: str, max_results: int = 5) -> str:
    """Search the web via Tavily, then use Groq LLM to provide a concise answer."""
    # Step 1: Tavily search
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": question,
        "max_results": max_results,
        "search_depth": "basic",
        "include_answer": True,
    }
    search_response = httpx.post(url, json=payload, timeout=30)
    search_response.raise_for_status()
    search_data = search_response.json()

    # Build context from search results
    context_parts = []
    if search_data.get("answer"):
        context_parts.append(f"Tavily Quick Answer: {search_data['answer']}")
    for result in search_data.get("results", []):
        context_parts.append(
            f"- {result.get('title', '')}: {result.get('content', '')[:400]}"
        )
    context = "\n".join(context_parts)

    # Step 2: Groq LLM to synthesize answer
    groq_url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    groq_payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Use the provided search results "
                    "to answer the user's question clearly and concisely."
                ),
            },
            {
                "role": "user",
                "content": f"Question: {question}\n\nSearch Results:\n{context}",
            },
        ],
        "temperature": 0.3,
        "max_tokens": 1024,
    }
    groq_response = httpx.post(groq_url, headers=headers, json=groq_payload, timeout=30)
    groq_response.raise_for_status()
    groq_data = groq_response.json()

    answer = groq_data["choices"][0]["message"]["content"]
    return answer


if __name__ == "__main__":
    mcp.run()
