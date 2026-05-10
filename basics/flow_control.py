# If/Else: Talking about the if/else, it is used for conditional statements. Suppose if there is a condition, if you do this,
# else you will get that, like this, for example:
if 2 > 1:
    print(True)
else:
    print(False)

# Loop: These are used when you want to use something again and again. Or you want to execute some task instantly or 
# you want to iterate something, like list or something.
# There are two types of loop: for loop and while loop
# For loop
for i in range(5):
    print(i)
# While loop
i = 5
while i > 0:
    print(i)
    i = i - 1

# break and continue
# break is used when you want to come out of the loop
# continue is used when you want to skip a line in loop or want to skip any condition and jump to next
# break is used by writing break and continue is used by writing continue

# Nested loop: Nested loop is a concept of loop inside loop, example:
for i in range(5):
    for n in i:
        pass  # pass is used when you dont know what to do next so you write this as a placeholder so that code does not break
