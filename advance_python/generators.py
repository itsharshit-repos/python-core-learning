# GENERATORS
# generators are special iterators suppose we have 1 million items, huge_list  = [1 million items], we can:
# generate values one-by-one lazily.
# Generators means produce values gradually instead of storing everything.
# Normal function: 
# def numbers():
#     return [1,2,3]
# creates all values immediately.
# Generator function:
# def numbers():
#     yield 1
#     yield 2
#     yield 3     (yield pauses function)
# It's like, run -> pause, resume -> pause, resume -> pause, like controlled streaming
# Example:
def test():
    print("A")
    yield 1
    print("B")
    yield 2
g = test()
print(next(g))
print(next(g))
# Function state pauses at yield !
# Another example:
def nums():
    for x in range(10):
        yield x
n = nums()
print(next(n))
print(next(n)) # This is now memory efficient, scalable and streaming based
# Generators are lazy computation means compute only when needed.

# Now this is a very beautiful sample example for token streaming, where this generator concept is used. 
import time
# Simulates an AI model emitting text tokens
def mock_ai_stream(prompt):
    response_text = "Token streaming feels fast because it reduces perceived latency."
    tokens = response_text.split(" ")  # Split into simulated chunks
    for token in tokens:
        time.sleep(0.3)  # Simulate network/generation delay
        yield token + " "  # Yield one piece at a time
# Reads the stream live
print(f"Prompt: What is token streaming?\nResponse: ", end="")
# The loop consumes the generator in real-time
for chunk in mock_ai_stream("What is token streaming?"):
    print(chunk, end="", flush=True)  # flush=True forces instant rendering
# MOST IMPORTANT: Instead of "generate everything → send once"
# we did, "generate → emit → generate → emit"

# Generator Expressions (The One-Liner Generator) Just like you can make a list in one line (List Comprehension), 
# you can make a generator in one line using parentheses () instead of square brackets []. EXAMPLE -
# List comprehension: Destroys RAM because it builds the whole list instantly
huge_list = [x for x in range(10000000)] 
# Generator expression: Uses almost zero RAM because it calculates on the fly
lazy_gen = (x for x in range(10000000))  # This parenthesis
print(next(lazy_gen))  # 0
print(next(lazy_gen))  # 1

# 'yield from': If you have a generator that needs to output items from another collection (like a list or a sub-generator), 
# you do not need to write a nested for loop. You can use 'yield from'.
# The long way
def old_way():
    tokens = ["AI", "is", "fun"]
    for t in tokens:
        yield t
# The trick way (Cleaner and faster)
def clean_way():
    tokens = ["AI", "is", "fun"]
    yield from tokens  # Automatically loops and yields each item

# Turning Generators into Pipelines (Chaining). You can pass one generator directly into another generator. 
# This allows you to build data preprocessing pipelines where data flows through functions step-by-step without saving 
# intermediate results to your hard drive or RAM.
def get_numbers():
    for i in range(1, 4):
        yield i  # Yields: 1, 2, 3
def square_numbers(numbers):
    for n in numbers:
        yield n * n  # Yields: 1, 4, 9
# Chain them together
raw_data = get_numbers()
processed_data = square_numbers(raw_data)
for result in processed_data:
    print(result)  # Outputs: 1, 4, 9