# Suppose we have any word, number or anything, and now we have to find them or get them, or we have to answer, is there any (#name)
# in this sentence? Does this text start with 'hello'? Python needs a way to search pattern, and general terms like 'in' in python
# won't work. So here comes the REGEX, it helps all of these, using some expressions.
# First, to use REGEX we need to import regex (regular expressions)
import re

#===============================================================================================================================

# Now first REGEX, lets find a digit.
# Symbol: \d means Find one digit
text = "AI in 2026"
result = re.search(r"\d", text)   # This line means 'search inside text'. ALSO 'r' means raw string
print(result.group())  # OUTPUT: 2 because it is for only getting 1 digit | ALSO this line means 'show what you found'.
# search() means "Look through text and stop at first match"
# Another example -
text = "Harshit"
result = re.search("a", text)
print(result.group())  # This is REGEX too, plain letters also work. REGEX doesn't always need symbols.

#===============================================================================================================================

# Now findall()
# Imagine now we want every digit, for that re.findall() meaning "Find all matches"
text = "AI in 2026"
result = re.findall(r"\d", text)
print(result)  # Notice this time we didn't used .group() because this findall() returns the list of digits

#===============================================================================================================================

# Now '+' in \d or anywhere else very important
# Because now suppose you don't want only one number, you want all numbers, BUT not as a [list] but proper '2026', so for that,
text = "AI in 2026"
result = re.findall(r"\d+", text)
print(result)  # Output: ['2026']
# OR
text = "AI in 2026"
result = re.search(r"\d+", text)
print(result.group())   # Output: 2026 (Simple and clear)
# '+' joins continuous digits
# Another example -
text = "AI 123 and 45"
result = re.findall(r"\d+", text)
print(result)  # Output: ['123', '45']
# OR
text = "AI 123 and 45"
result = re.search(r"\d+", text)
print(result.group())  # But this version will not print 45 after 123, We will talk about this later

#===============================================================================================================================

# Now search is one thing, WE WANT "Clean text"
# So for that, we use re.sub() meaning 'substitute/replace'
text = "AI!!!"
clean = re.sub("!", "", text)  # This line means substitute '!' with '(#nothing)' from text
print(clean)
# Another example -
text = "Hello###"
clean = re.sub("#", "", text)
print(clean)

#===============================================================================================================================

# '\w' is WORD CHARACTER
# \w means match a single word character, this includes, letters (a-z, A-Z), digits (0-9) and underscore (_)
text = "AI_2026!"
print(re.findall(r"\w", text))
# AND again just like previous '+' joins continuous words
print(re.findall(r"\w+", text)) # means keep collecting words characters continuously
# Another example -
text = "GPT_4 and AI"
print(re.findall(r"\w+", text))

#===============================================================================================================================

# '.' DOT Means match any single character
text = "AI!"
print(re.findall(r".", text))
# AND again just like previous '+' joins continuous words
print(re.findall(r".+", text)) # Take all the character at once and print in form of a list, [AI!]
# '.' means everything like it can even take space also in list like ['a','','i']

#===============================================================================================================================

# '*' Means zero or more 
# Example -
text = "aaa b"
print(re.findall(r"a*", text))  # Output is ['aaa', '', '', '']
# Output like this because REGEX can match: many 'a' or zero 'a', That's why * can create empty matches
# Another example -
text = "abc"
print(re.findall(r"z*", text)) # Output will be: ['', '', '', ''] because same there are NO 'z', that is why it took zero 'z' and 
# print empty ['', '', '', '']

#===============================================================================================================================

# '\s' is Space characters Means match whitespace
# This includes space (''), tab and new line
# Example -
text = "AI GPT"
print(re.findall(r"\s", text))  # Output is [' '] means got it's whitespace
# Another example -
text = "AI   GPT"
print(re.findall(r"\s", text))  # Output is [' ', ' ', ' '] means 3 whitespaces
# But now again you want them togerther, then again we will use the '+'
print(re.findall(r"\s+", text))  # Output is ['   ']

#===============================================================================================================================

# "^" is Start with. Means match 'beginning of string'
text = "AI Model"
print(re.findall(r"^AI", text))  # Output is ['AI'], means this line concludes, Is the line starting with word 'AI'?, if yes, Print
# If no, then return []
# Another example for empty return
print(re.findall(r"^Model", text))  # Output is [] No match because its NOT starting with Model

#===============================================================================================================================

# '$' is Ends with. Means match end
text = "model.py"
print(re.findall(r"py$", text))  # Output is ['py'] ends with py
# Another example -
print(re.findall(r"txt$", text))  # Output is [] because its NOT ending with txt

#===============================================================================================================================

# '[]' is Choices/Ranges. Means inside brackets choose one from here
text = "cat bat hat"
print(re.findall(r"[cb]", text))  # This line means match c or b result: ['c','b']
# Now learn Range [0-9] means digit
text = "AI25"
print(re.findall(r"[0-9]", text))  # This line looks for the digit ranging between 0-9 in text! hence output ['2','5']
# Range for letters, in two forms wither lowercase or uppercase
text = "AIgpt"
print(re.findall(r"[a-z]", text))  # It will sellect all lower case words from text, output: ['g', 'p', 't']
# [a-z] for range in lowercase and [A-Z] for range in uppercase, and '+' can be applied here also

#===============================================================================================================================