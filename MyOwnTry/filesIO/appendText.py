appendLine=input("Press Enter to append text to the file...")
with open("MyOwnTry/filesIO/Text.txt", 'a+') as file:
    file.write('\n' + appendLine)