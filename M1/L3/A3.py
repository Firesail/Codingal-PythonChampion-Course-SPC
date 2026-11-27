# 1. Creation & Basic Info
text = "  Hello, Python World!  "
print("Original:", repr(text))
print("Length:", len(text))               # Total characters including spaces

# 2. Cleaning & Case Conversion
clean = text.strip()                      # Remove leading/trailing whitespace
print("Stripped:", clean)
print("Upper:", clean.upper())            # 'HELLO, PYTHON WORLD!'
print("Lower:", clean.lower())            # 'hello, python world!'
print("Title:", clean.title())            # 'Hello, Python World!'
print("Swapcase:", clean.swapcase())      # 'hELLO, pYTHON wORLD!'

# 3. Indexing & Slicing
print("First char:", clean[0])            # 'H'
print("Last char:", clean[-1])            # '!'
print("Slice [7:13]:", clean[7:13])       # 'Python'
print("Reversed:", clean[::-1])           # '!dlroW nohtyP ,olleH'

# 4. Searching & Checking
print("Contains 'Python':", "Python" in clean)  # True
print("Index of 'Python':", clean.find("Python")) # 7 (-1 if not found)
print("Count of 'o':", clean.count("o"))          # 3
print("Starts with 'Hello':", clean.startswith("Hello")) # True
print("Is numeric ('123'):", "123".isdigit())     # True
print("Is alphabetic ('abc'):", "abc".isalpha())  # True

# 5. Modifying, Splitting & Joining
replaced = clean.replace("World", "Developers")
print("Replaced:", replaced)              # 'Hello, Python Developers!'

words = clean.split(" ")                  # Split into list: ['Hello,', 'Python', 'World!']
print("Split list:", words)

joined = "-".join(words)                  # Join list into string: 'Hello,-Python-World!'
print("Joined:", joined)

# 6. Concatenation, Repetition & Formatting
greeting = "Hi" + " " + "there!"          # Concatenation
echo = "Ha" * 3                           # Repetition: 'HaHaHa'
lang, ver = "Python", 3.12
formatted = f"{greeting} Welcome to {lang} {ver} ({echo})."
print("Formatted:", formatted)
