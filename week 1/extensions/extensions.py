def main():
    name = input("FileName: ").lower().strip()
    file_types(name)






def file_types(name):

    if name.endswith('.gif'):
        print("image/gif")
    elif name.endswith('.jpg') or name.endswith('.jpeg'):
        print("image/jpeg")
    elif name.endswith('.pdf'):
        print("application/pdf")
    elif name.endswith('.png'):
        print("image/png")
    elif name.endswith('.txt'):
        print("text/plain")
    elif name.endswith('.zip'):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
