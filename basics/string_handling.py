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
