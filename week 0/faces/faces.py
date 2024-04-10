def convert(f):
    f = f.replace(":)", "🙂")

    f = f.replace(":(", "🙁")
    return f

faces = input("Text: ")
print(convert(faces))
