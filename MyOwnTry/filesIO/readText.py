try:
    with open("MyOwnTry/filesIO/Text.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")