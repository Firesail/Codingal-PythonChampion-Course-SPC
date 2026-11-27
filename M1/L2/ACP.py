# Store birthdays using names as keys and dates as values
birthdays = {
    "Alice": "1995-06-15",
    "Bob": "1998-11-22",
    "Charlie": "2001-03-09"
}

# Add a new birthday
birthdays["Diana"] = "1997-08-30"

# Look up a birthday
name = input("Enter a name to look up: ")
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, no birthday found for {name}.")
