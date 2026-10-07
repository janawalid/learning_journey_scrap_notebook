# Week 1, Day 2

## Type Hints
- What are they?
A guide for the developer and IDE to know what data type should be used. Python ignores it at runtime, but the IDE uses it for autocomplete and mypy uses it for static analysis.

- Why use them?
early bug detection , also makes ide provide better autocomplete suggestions

- Basic syntax for functions
parameter: datatype -> datatype

- How to check them (mypy)
run mypy on the file

## Pydantic
- What is it?
a library that helps in data validation , unlike mypy this blocks excution if the data type is wrong

- Difference from type hints
this is not a suggestion ,if the data type is missmatched it will block the excution of the code

- Validation (data in)
The schema that Pydantic validates against is generally defined by Python type hints.

- Serialization (data out)
ydantic provides functionality to serialize model in three ways:

To a Python dict made up of the associated Python objects.
To a Python dict made up only of “jsonable” types.
To a JSON string.

- What happens with wrong data?
it raises an error of what exactly is wrong

## AsyncIO
- What is it?
a library that helps us run tasks async, so it makes preformance better, as while it waits for a respond from a certain task, it starts another one

- When to use it?
when i have to run multiple calls or tasks and running them sequentially would take a lot of time

- Key syntax (async def, await, gather)
async def defines async function, await waits for async operation, asyncio.gather(*tasks) runs multiple tasks in parallel 

- The for loop trap
Putting await inside a for loop makes it sequential (slow). Create tasks first, then gather them for parallel execution

- Real result: sync time vs async time
Sync took ~2.8 seconds, async took ~1.2 seconds for the same 4 URLs

- Why was async faster?
While waiting for HTTP responses, the event loop could send other requests instead of blocking

## httpx
- What is it?
Modern HTTP library for making web requests
- Why use it instead of requests? 
httpx supports both sync and async; requests only supports sync

## Unpacking Operators
- What does * do?
* unpacks lists/tuples into positional arguments

- What does ** do?
** unpacks dicts into keyword arguments
