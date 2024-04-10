text = input("Enter text: ")
new_text = ""

for char in text:
    if char.lower() not in "aeiou":
        new_text += char

print(new_text)
