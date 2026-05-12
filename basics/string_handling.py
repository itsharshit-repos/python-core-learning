# STRING SLICING
# So 'String' is a sequence of character. 
# For example: H  A  R  S  H  I  T
# Indexing:    0  1  2  3  4  5  6   (means every character has position)
# -ve Index:  -7 -6 -5 -4 -3 -2 -1
name = 'Harshit'
print(name[0])  # prints 'H'
print(name[-1])
# Strings are Immutable means cannot be changed because strings cannot modify individual character directly.
# So to change string you can:
name = 'K' + name[1:]  # Added one character in beginning and started name string from first position and joined them
print(name)
# Now taking part of string like [start:end:steps], steps means if you want to print skipping any place in between
print(name[0:4])
print(name[0:5:2])  # taking the step of 2
word = "Python"
print(word[-4:-1])
# To reverse a string you can use (::-1)
print(word[::-1])
print(word[5:1:-1])
print(word[4:0:-2])

# STRING METHODS
# 1. lower() to convert in lowercase
print(word.lower())
# 2. upper() to convert in uppercase
print(word.upper())
# Strings are immutable so it does not change string permanently because methods return new string, original unchanged!
# 3. strip() to remove spaces from beginning/end
text = "   hello   " # (useful bcz user input contains unwanted spaces.)
print(text.strip())
# 4. replace() to replace part of string
txt = 'I like Java'
print(txt.replace('Java', 'Python'))
# 5. find() to find position of sub-string
tex = "Artificial"
print(tex.find("fic"))
# 6. split() to break things into list
text = "AI systems engineering"
print(text.split())
# 7. join() oppisite of split
wrd = ['AI', 'systems', 'engineering']
print("-".join(wrd))

# METHOD CHAINING
sentence = "   artificial intelligence systems   "
print(sentence.strip().upper())  # using multiple method in single line
# example:
d = "   backend engineering with python   "
print(d.strip().upper().replace("PYTHON", "FASTAPI"))
print("-".join(sentence.split()))

# f-String: f means formatted strings
age = 18
print(f"My name is {name} and I am {age} years old")
# question: Print exactly "Harshit is learning AI Systems Engineering using Python"
name = "Harshit"
domain = "AI Systems Engineering"
language = "Python"
print(f"{name} is learning {domain} using {language}")

# ESCAPE CHARACTERS: Sometimes you need special formatting
# 1. \n means new line
print("Hello\nWorld")
# 2. \t means tab spacing
print("AI\tSystems")
# 3. \"\" means quote inside string
print("He said \"Hello\"")
# 4. r"" means RAW string, with this python dont treat \ as escape character
path = r"C:\Users\Harshit"

# MEMBERSHIP OPERATORS: (Very Important for validation, search systems, AI preprocessing, parsers, backend logic)
# python gives in, not in. Example:
text = "Artificial Intelligence"
print("Intel" in text)   # prints True because substring exist
print("Backend" not in text)   # opposite check prints True
# memberships checks are case-sensetive. p != P. Always take care of this, this causes many real bugs
text = "Python"
print("python" in text)

