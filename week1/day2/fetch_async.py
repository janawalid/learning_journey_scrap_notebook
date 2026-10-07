import asyncio
import time
import httpx

urls = urls=[
    "https://docs.python.org/3/library/asyncio.html",
    "https://www.python-httpx.org/",
    "https://en.wikipedia.org/wiki/Egypt",
    "https://en.wikipedia.org/wiki/Dexter_(TV_series)",
    "https://fake_url.com"
]

async def fetch_url(client: httpx.AsyncClient, url: str):
      try:
            response = await asyncio.wait_for(client.get(url), timeout=10.0)
            return f"Fetched {url}: {len(response.text)} bytes"
      except asyncio.TimeoutError:
            return f"Timeout occurred while fetching {url}"
      except httpx.HTTPError as e:
            return f"HTTP error occurred while fetching {url}: {e}"
    
    

async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
            tasks = [fetch_url(client, url) for url in urls]
            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(response)
    end = time.time()

    print(f"Total time: {end - start} seconds")

asyncio.run(main())