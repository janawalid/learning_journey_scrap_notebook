import httpx
import time

urls=[
    "https://docs.python.org/3/library/asyncio.html",
    "https://www.python-httpx.org/",
    "https://en.wikipedia.org/wiki/Egypt",
    "https://en.wikipedia.org/wiki/Dexter_(TV_series)"
]

start = time.time()
for i in urls:
    r = httpx.get(i)
    print(f"Fetched {i}: {len(r.text)} bytes")

end = time.time()
print(f"Total time: {end - start} seconds")