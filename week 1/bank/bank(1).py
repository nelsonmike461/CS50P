hey = input("Greeting: ").strip().lower()

if hey.startswith('hello'):
    print("$0")
elif hey.startswith('h'):
    print("$20")
else:
    print("$100")
