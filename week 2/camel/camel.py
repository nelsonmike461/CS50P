def main():
    user_text = input("camelCase: ")
    print("snake_case: ", camel_to_snake(user_text))



def camel_to_snake(text):
    result = [text[0].lower()]
    for c in text[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            result.append('_')
            result.append(c.lower())
        else:
            result.append(c)
    return ''.join(result)

main()
