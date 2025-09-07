# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The lower() method returns the string in lower case:
a = "HELLO, WORLD!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))

# Learn more about String Methods with our String Methods below Reference

# https://www.w3schools.com/python/python_ref_string.asp

# Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

