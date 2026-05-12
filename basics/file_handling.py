# FILE: A file is a data stored permanently on disk

# OPENING A FILE: open("filename", "mode")
# example: test = open("test.txt", "r")  
# 'r' stands for read mode means read existing file
# 'w' stands for write mode means writing into the existing file. Create file is absent and completely overwrite old content.
# 'a' stands for append mode means add content at end and does not erase old content. For log, chat history, AI output, etc

# First program:
file = open("demo.txt", "w")
file.write("Hello world")
file.close()  # Very important. Always close the file after work. Because operating system keeps resource allocated. 
# Unclosed files can cause memory/resource issues, corrupted writes, locked files.

# Reading the File
file = open("demo.txt", "r")
data = file.read()
print(data)
file.close()
# read() reads full file content and store it as string.

# Append mode
file = open("demo.txt", "a")
file.write("\nNew line")
file.close()
# output: Hello world
#         New line

# MOST IMPORTANT MODERN WAY is to use CONTEXT MANAGER!
# Professionaly python code usually uses: with open()
# Because it automatically close the file, even if error happens. Very important engineering practice.
# Suppose 'with' means 'use resource safely'
# open with("filename", "mode")
# EXAMPLE: 
# Write program that:
# creates file "notes.txt"
# writes "AI Systems Engineering"
# appends "Python Backend"
# reads and prints full file
with open("notes.txt", "w") as testing:
    testing.write("AI System Engineering")
with open("notes.txt", "a") as testing:
    testing.write("\nPython Backend")
with open("notes.txt", "r") as testing:
    print(testing.read())

# To get data line by line, professionally use for loop for huge set of dataset or file.
# Because it is memory efficient, process line by line and scalable.
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())  # .strip() is used here to avoid extra spacing

# FILE POINTER/CURSOR
# pointer tracks current reading position
# Resetting pointer - seek(), you can move pointer manually. Example:
with open("demo.txt", "r") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
# Question to solve:
# Create file: data.txt
# Content:
# Python
# AI
# Systems
# Then: read full file once, use seek(0), read again, print both outputs with labels using f-strings
with open("data.txt", "w") as f:
    f.write("Python\n")
    f.write("AI\n")
    f.write("Systems\n")
with open("data.txt", "r") as f:
    print(f"First read:\n{f.read()}")
    f.seek(0)
    print(f"Second read:\n{f.read()}")

# BINARY FILES: computers fundamentally store everything as binary
# File modes for binary: earlier it was 'r','w','a'
# 'rb', 'wb', 'ab', b means binary mode
# example of reading birany:-
with open("image.png", "rb") as file:
    data = file.read()
print(data[:10])   # output may look like: b'\x89PNG\r\n\x1a\n', THIS is raw byte data.
# very useful in networking, APIs, sockets, databases, etc

# ENCODING:
# Computers do not understand characters directly, they understand numbers/bytes.
# Encoding converts characters to bytes. Most common encoding is UTF-8. Wrong encoding can corrupt data. That is why UTF-8 is standard.
# Example:-
text = "AI"
encoded = text.encode()
print(encoded)   # output: b'AI', NOW it became bytes.

# DECODING:
data = b'AI'
print(data.decode())
